document.addEventListener('DOMContentLoaded', function () {
    // Находим все элементы с классом language-switch
    const languageSwitches = document.querySelectorAll('.language-switch');

    // Получаем текущий язык из URL
    const currentLanguage = window.location.pathname.split('/')[1];

    // Перебираем найденные элементы и назначаем обработчик событий
    languageSwitches.forEach(function (languageSwitch) {
        // Получаем язык из атрибута data-language
        const selectedLanguage = languageSwitch.getAttribute('data-language');

        // Проверяем, если текущий язык совпадает с выбранным, добавляем класс active-language
        if (selectedLanguage === currentLanguage) {
            languageSwitch.classList.add('active-language');
        }

        // Назначаем обработчик событий для переключения языка
        languageSwitch.addEventListener('click', function () {
            // Получаем выбранный язык
            const selectedLanguage = languageSwitch.getAttribute('data-language');

            // Формируем новую ссылку с выбранным языком
            const newUrl = window.location.href.replace('/' + currentLanguage + '/', '/' + selectedLanguage + '/');

            // Переходим по новой ссылке
            window.location.href = newUrl;
        });
    });
});
