document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.dropdown-submenu > .dropdown-item.dropdown-toggle').forEach(function(el) {
        el.addEventListener('click', function(e) {
            e.stopPropagation();
            e.preventDefault();
            this.parentNode.querySelector('.dropdown-menu').classList.toggle('show');
        });
    });
});
