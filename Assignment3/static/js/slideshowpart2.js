


function BuildSlideShow(){

  var xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {

      var myObj = JSON.parse(this.responseText);

        console.log(myObj);

        list_images = myObj.images;

        total_images = list_images.length

        for (i = 0; i < total_images ; i++) {


            var div_img = document.createElement('div');
            div_img.setAttribute('class', 'mySlides fade');
            div_img.setAttribute('id', 'img'+i);
            document.getElementById("slideshow").appendChild(div_img);

            console.log('image is set');

            n = i + 1;
            var numbertext_div = document.createElement('div');
            numbertext_div.setAttribute('class', 'numbertext');
            numbertext_div.textContent = n + ' / ' + total_images;
            document.getElementById('img'+i).appendChild(numbertext_div);

            var img_el = document.createElement('img');
            img_el.setAttribute('src', list_images[i].path );
            img_el.setAttribute('style', 'width:100%');
            document.getElementById('img'+i).appendChild(img_el);


            var caption_el = document.createElement('div');
            caption_el.setAttribute('class', 'text');
            caption_el.textContent = list_images[i].caption;
            document.getElementById('img'+i).appendChild(caption_el);

            var span_el = document.createElement('span');
            span_el.setAttribute('class', 'dot');
            document.getElementById('dots_for_control').appendChild(span_el);

        }
    }

  };

  xmlhttp.open("GET", "http://127.0.0.1:8000/static/json_files/all_images.json", true);
  xmlhttp.send();

};

var slideIndex = 0;
function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  console.log(slides.length);
  console.log(document.getElementById('img1'));

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";

  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";

  setTimeout(showSlides, 2000);
}


BuildSlideShow();

setTimeout(showSlides, 100);
