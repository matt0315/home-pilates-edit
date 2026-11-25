/**
 * Rewrites product links from /data/links.json so tracking tags
 * can be added in one place later, without editing every page.
 *
 * Usage on a page:
 *   <script src="js/links.js" data-links="data/links.json" defer></script>
 *
 * Config:
 *   tags.amazon — Amazon Associates AU tracking ID (appended as ?tag=)
 *   products[id].trackedUrl — full network deep link (Commission Factory, Awin, Impact, etc.)
 *   products[id].url — untagged retailer URL, used until trackedUrl or a tag is set
 */
(function () {
  var script = document.currentScript;
  var src = script && script.getAttribute("data-links");
  if (!src) return;

  function withAmazonTag(url, tag) {
    if (!tag) return url;
    try {
      var u = new URL(url, window.location.href);
      if (!/(^|\.)amazon\.com\.au$/i.test(u.hostname)) return url;
      u.searchParams.set("tag", tag);
      return u.toString();
    } catch (e) {
      return url;
    }
  }

  function resolve(product, tags) {
    if (!product) return null;
    if (product.trackedUrl) return product.trackedUrl;
    var tag = tags && tags.amazon;
    if (product.network === "amazon" || (product.url && product.url.indexOf("amazon.com.au") !== -1)) {
      return withAmazonTag(product.url, tag);
    }
    return product.url;
  }

  fetch(src, { credentials: "same-origin" })
    .then(function (res) {
      if (!res.ok) throw new Error("links.json " + res.status);
      return res.json();
    })
    .then(function (data) {
      var products = (data && data.products) || {};
      var tags = (data && data.tags) || {};
      var nodes = document.querySelectorAll("[data-product-link]");
      nodes.forEach(function (el) {
        var id = el.getAttribute("data-product-link");
        var href = resolve(products[id], tags);
        if (href) el.setAttribute("href", href);
      });
    })
    .catch(function () {
      // Leave the untagged hrefs already in the HTML.
    });
})();
