// Меню пользователя в правом верхнем углу: открыть по клику, закрыть по клику вне меню или Esc
(function () {
    var menu = document.querySelector('.user-menu');
    if (!menu) return;
    var button = menu.querySelector('.user-menu__button');

    function setOpen(open) {
        menu.classList.toggle('is-open', open);
        button.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    button.addEventListener('click', function (event) {
        event.stopPropagation();
        setOpen(!menu.classList.contains('is-open'));
    });

    document.addEventListener('click', function (event) {
        if (!menu.contains(event.target)) setOpen(false);
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') setOpen(false);
    });
})();
