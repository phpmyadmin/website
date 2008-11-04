var book_counter = 1;
var book_array = new Array(4);

/**
 * Function which is called on page load.
 */
function onLoadHandler() {
    /* If page contains bookbanner element, enable banners rotating */
    if (document.images && document.bookbanner) {
        book_array[0] = new Image(97,123);
        book_array[0].src = "${base_url}images/books/pma_en_100x123.png";
        book_array[1] = new Image(90,122);
        book_array[1].src = "${base_url}images/books/pma_cz_90x122.jpg";
        book_array[2] = new Image(90,122);
        book_array[2].src = "${base_url}images/books/pma_de_90x122.jpg";
        book_array[3] = new Image(100,123);
        book_array[3].src = "${base_url}images/books/pma_es_100x123.png";
        window.setInterval("changeBookBanner()", 10000);
    }
}

/**
 * Function to rotate book banners.
 */
function changeBookBanner() {
    if(book_counter > 3)
       book_counter = 0;
    document.bookbanner.src = book_array[book_counter].src;
    book_counter++;
}

/* Activate onLoad handler */
window.onload = onLoadHandler;
