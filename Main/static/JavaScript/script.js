/* This script is mainly for the conversion of dates to sweet human readable fashion */

const convertDates = (inputDate) => { //Input date in yyyy-mm-dd format
    const months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    };
    const rest_ = inputDate.split('-'); // Splits the inputDay whose format is like: 2022-02-12
    return `${parseInt(rest_[2])} ${months[parseInt(rest_[1])]}, ${parseInt(rest_[0])}`;
}

const dateElement = document.querySelectorAll('div#date');
dateElement.forEach(elem => {
    // Gets all the elements bearing the id: date and changes the date format
    elem.textContent = convertDates(elem.textContent);
})