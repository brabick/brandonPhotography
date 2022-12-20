function scrollerington() {
    let element = document.getElementById("carouselIndicators")
    let maxScrollLeft = element.scrollWidth - element.clientWidth;
    //alert(maxScrollLeft);
    let left = event.clientX - element.offsetLeft;
    //alert(left);
    if (maxScrollLeft <= left) {
        //alert(element.scrollLeft);
        element.scrollLeft += (left / 3);
    } else {
        //alert(element.scrollLeft);
        element.scrollLeft -= (left);
    }
}
