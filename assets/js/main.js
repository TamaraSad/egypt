(function () {
  'use strict';

  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  var toTop = document.querySelector('.to-top');

  /* Мобильное меню */
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'إغلاق القائمة' : 'فتح القائمة');
    nav.classList.toggle('is-open', open);
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setMenu(false);
    });
    window.matchMedia('(min-width: 1001px)').addEventListener('change', function (mq) {
      if (mq.matches) setMenu(false);
    });
  }

  /* Тень шапки и кнопка «наверх» */
  var ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle('is-scrolled', y > 10);
    if (toTop) toTop.classList.toggle('is-visible', y > 700);
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();

  /* FAQ: открыт только один вопрос */
  var faqItems = document.querySelectorAll('.faq details');
  faqItems.forEach(function (item) {
    item.addEventListener('toggle', function () {
      if (!item.open) return;
      faqItems.forEach(function (other) {
        if (other !== item) other.open = false;
      });
    });
  });

  /* Логотип в подвале: если файла нет, показываем название текстом */
  var logo = document.querySelector('.brand-logo img');
  if (logo) {
    var markMissing = function () { logo.parentNode.classList.add('is-missing'); };
    if (logo.complete && logo.naturalWidth === 0) markMissing();
    else logo.addEventListener('error', markMissing);
  }

  /* Текущий год в подвале */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
