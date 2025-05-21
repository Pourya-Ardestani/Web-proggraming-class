const fillSrc = "../src/images/selected-product/star-filled.svg";
const emptySrc = "../src/images/selected-product/star-empty.svg";
const children = document.body.children;
function changeStar(img) {
  if (img.src.includes("star-filled.svg")) {
    img.src = emptySrc;
  } else {
    img.src = fillSrc;
  }
}

function closeWindow() {
  document.getElementById("comment-window").style.display = "none";
//   document.getElementsByTagName('body')[0].classList.remove('blurred');
for (let i = 0; i < children.length; i++) {
        const el = children[i];
        if (el.id !== 'comment-window') {
            el.classList.remove('blurred');
        }
    }
}

function openWindow(){
    document.getElementById("comment-window").style.display = "flex";
    // document.getElementsByTagName('body')[0].classList.add('blurred');
    for (let i = 0; i < children.length; i++) {
        const el = children[i];
        if (el.id !== 'comment-window') {
            el.classList.add('blurred');
        }
    }
    

}
