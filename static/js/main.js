$('.close').click(function(){
    $('video').each(function(){
      $(this).get(0).pause();
    })
  });



  const Nlink = document.getElementById("Nlink");
  const navbar = document.getElementById("full-nav");
  const navIcon = document.getElementById("nav-icon")

  Nlink.addEventListener("click", function() {
    navbar.style.display = (navbar.style.display === "none") ? "block" : "none";
  });
  navIcon.addEventListener("click", function() {
    navbar.style.display = (navbar.style.display === "") ? "block" : "";
  });



  $(".nav-icon").click(function() {
    $(".full-nav").addClass("open");
  });
  $(".nav-close").click(function() {
    $(".full-nav").removeClass("open");
  });
  $(window).scroll(function() {
    var sc = $(window).scrollTop();
    if (sc > 100) {
      $(".nav").addClass("sticky");
    } else {
      $(".nav").removeClass("sticky");
    }
  });

  function changeNavbarColorOnScroll() {
  const navbarElement = document.querySelector('.navbar');
  const navbarIconElement = document.querySelector('.naviconimage');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
      navbarElement.style.backgroundColor = '#fff';
      navbarIconElement.style.filter = 'none';
    } else {
      navbarElement.style.backgroundColor = '';
      navbarIconElement.style.filter = '';
    }
  });
}

// Call the function when the DOM is ready
document.addEventListener('DOMContentLoaded', changeNavbarColorOnScroll);



  



document.body.addEventListener('htmx:configRequest', (event) => {
event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
})
