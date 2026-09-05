function startNavigator() {
  document.getElementById('navigator').classList.add('active');
  document.getElementById('navigator').scrollIntoView({ behavior: 'smooth' });
}

function choose(el, value) {
  document.querySelectorAll('.choice').forEach(b => b.classList.remove('selected'));
  el.classList.add('selected');
  document.getElementById('result').classList.add('show');

  // Optional: call the Flask backend for guidance instead of a static message.
  fetch('/api/rights', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ selection: value })
  })
    .then(res => res.json())
    .then(data => {
      const resultEl = document.getElementById('result');
      resultEl.querySelector('br').nextSibling &&
        (resultEl.childNodes[2].textContent = data.message);
    })
    .catch(() => {
      // Silently fall back to the static message already shown in the HTML.
    });
}
