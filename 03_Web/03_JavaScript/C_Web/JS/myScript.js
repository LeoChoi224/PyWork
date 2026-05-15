
const light = function(sw) {
    let pic;

    if (sw == 0){
        pic = "https://www.w3schools.com/html/pic_bulboff.gif";
    } else {
        pic = "https://www.w3schools.com/html/pic_bulbon.gif";
    }

    document.getElementById('myImage').src = pic;
	// element객체.attribute이름
    // id 값 'myImage' 를 가진 element 를 찾아서 
    // 'src' attribute 값을 변경    
}
