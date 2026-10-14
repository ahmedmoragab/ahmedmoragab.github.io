// Use one shared path so visiting several pages counts as one site visit per session.
// Keep Sessions enabled and allow public visitor counts in GoatCounter settings.
(() => {
  if (window.location.hostname !== "ahmedmoragab.github.io") return;

  const endpoint = "https://ahmedragab.goatcounter.com";
  const path = "/site-visits";
  const script = document.createElement("script");
  script.async = true;
  script.src = "https://gc.zgo.at/count.js";
  script.dataset.goatcounter = `${endpoint}/count`;
  script.dataset.goatcounterSettings = JSON.stringify({ path, title: "Site visitors", no_events: true });
  document.head.appendChild(script);

  const counter = document.getElementById("site-visitor-count");
  const number = document.getElementById("site-visitor-number");
  if (!counter || !number) return;

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 5000);
  fetch(`${endpoint}/counter/${encodeURIComponent(path)}.json`, {
    signal: controller.signal,
    credentials: "omit",
  })
    .then((response) => {
      if (!response.ok) throw new Error("Visitor count unavailable");
      return response.json();
    })
    .then((data) => {
      const count = String(data.count ?? "");
      if (!/^\d[\d,\s.]*$/.test(count)) return;
      number.textContent = count;
      counter.hidden = false;
    })
    .catch(() => {
      // Do not show a fake zero or disrupt the page if analytics are blocked.
    })
    .finally(() => clearTimeout(timeout));
})();
