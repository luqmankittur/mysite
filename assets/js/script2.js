/*---- Logo ----*/
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
    var image = document.getElementsByClassName("logo")[0]; image.src = "/static/images/light1.png"
  }
/* -- Glow effect -- */

const blob = document.getElementById("blob");

window.onpointermove = event => {
  const { clientX, clientY } = event;

  blob.animate({
    left: `${clientX}px`,
    top: `${clientY}px`
  }, { duration: 4000, fill: "forwards" });
}

/*-------------------------------about--------------------*/

        var tablinks= document.getElementsByClassName("tab-links");
        var tabcontents= document.getElementsByClassName("tab-contents");

        function opentab(tabname){
            for(tablink of tablinks){
                tablink.classList.remove("active-link");
            }


            for(tabcontent of tabcontents){
                tabcontent.classList.remove("active-tab");
            }

            event.currentTarget.classList.add("active-link");
            document.getElementById(tabname).classList.add("active-tab")
        }

/*-------------------------------menu--------------------*/

        var sidemenu = document.getElementById("sidemenu")

        function openmenu(){
            sidemenu.style.right = "0"


        }

        function closemenu(){
            sidemenu.style.right = "-200px"
        }


/*-------------------------------message--------------------*/


    const scriptURL = 'https://script.google.com/macros/s/AKfycbw14LqMdZY_lmgepn2GjPv1L7AAdCxLUu96ERcx6D6N74VazurmSLcUjZ4YAWWCvz-p/exec'
    const form = document.forms['submit-to-google-sheet']
    const msg= document.getElementById("msg")

    form.addEventListener('submit', e => {
      e.preventDefault()
      fetch(scriptURL, { method: 'POST', body: new FormData(form)})
        .then(response => {
            msg.innerHTML="Message Sent."
            setTimeout(function(){
                msg.innerHTML=""
            },3000)
            form.reset()
        })
        .catch(error => console.error('Error!', error.message))
    })


    /*-------------------------------animation--------------------*/

    const observer= new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            console.log(entry)
            if(entry.isIntersecting) {
                entry.target.classList.add('show');
            }
            else{
                entry.target.classList.remove('show')
            }

        });
    });

    const hiddenElement =document.querySelectorAll('.hidden');
    hiddenElement.forEach((el)=> observer.observe(el));