function makeComment(){ //place comment after submit is pressed
var textvalue = document.getElementById("comment").value; //get value from textbox
if(textvalue != ""){ //check if the comment section is not empty
var div = document.createElement("div");
div.classList.add("commentreplies");
div.innerHTML = textvalue;

$.ajax({
  type: "POST",
  url: "views.post_new2.py",
  data: { param: textvalue}
})


//var data = textvalue;
//  $.post("{% url 'post_new2' %}", data, function(response){
//      if(response === 'success'){ alert('Yay!'); }
//      else{ alert('Error! :('); }
//  });

div.addEventListener("mouseenter", function(){
  shadowenter(div)
});
div.addEventListener("mouseleave", function(){
  shadowleave(div)
});
div.addEventListener("click", function(){
  reply(div,0)
});
var inner = document.createElement("div"); //create a new div that has the property being moved slightly
inner.classList.add("inner"); //add class that moves new div slighlty
document.getElementById("main").appendChild(div);
div.parentNode.insertBefore(inner, div.nextSibling);
document.getElementById('comment').value = ""; //make comment section empty again
}}

function shadowenter(div) { //create a shadow effect when hovering over comment
  div.classList.add("shadow");
}

function shadowleave(div) {//remove shadow effect when stop hovering over comment
  div.classList.remove("shadow");
}


function reply(div,number){ //Create a reply textbox
var inner = document.createElement("div");
var textinput = document.createElement("textarea");
var replysubmit = document.createElement("button");
var replydelete = document.createElement("button");
//create all elements for the new textbox with buttons to submit and delete textbox
var element = document.getElementById('innerid');//if there is a reply textbox already delete this one first
if(element){
  element.parentNode.removeChild(element);
}
inner.classList.add("form-textarea");
textinput.classList.add("form-control");
textinput.classList.add("beep");
replysubmit.classList.add("btn");
replysubmit.classList.add("btn-primary");
inner.classList.add("inner");
// add all classes to make comment box look good

replysubmit.innerHTML = "Submit";
replydelete.innerHTML = "X";
//add text to buttons
textinput.id = "textid";
replydelete.id = "replydelete";
inner.id = "innerid"

//set id's to find these boxes later
inner.classList.add("replyclass");
textinput.classList.add("replyclass");
replydelete.classList.add("replyclass");
replysubmit.classList.add("replyclass");
// add all elements to a combined class to find them as group later

if(number === 0){ //check if this is the first reply (then create new box)
div.nextSibling.parentNode.insertBefore(inner, div.nextSibling.nextSibling);}
else{ //if not the first reply add the reply box to other reply div
  div.parentNode.insertBefore(inner, div.nextSibling);
}
inner.appendChild(textinput);
inner.appendChild(replydelete);
inner.appendChild(replysubmit);
// add the textbox and buttons
replydelete.addEventListener("click", function(){
  deletereply(); //set listener for deleting the created reply box
});
replysubmit.addEventListener("click", function(){
  var textvalue1 = document.getElementById("textid").value;
  if(textvalue1 != ""){ //check if reply box is not empty
  submitreply(div) //set listener for submiting the reply
  deletereply(); //delete the reply box after having it submitted
}
});
};

function deletereply(replydelete){ //if reply textbox exists remove it
  var element = document.getElementById('innerid');
  if (element) {
    element.parentNode.removeChild(element);
  }
};


function submitreply(div){ //submit the created reply
var replycomment = document.createElement("div");//create div to place in the reply
var textvalue1 = document.getElementById("textid").value; //store value of reply textbox
replycomment.classList.add("commentreplies");
replycomment.innerHTML = textvalue1;

replycomment.addEventListener("mouseenter", function(){
  shadowenter(replycomment) //create a shadow effect when hovering over comment
});
replycomment.addEventListener("mouseleave", function(){
  shadowleave(replycomment) //remove shadow effect when stop hovering over comment
});
replycomment.addEventListener("click", function(){
  reply(replycomment,1)
  //when the replied comment is pressed create a reply textbox to reply to the reply the 1 stand for that it is not the first reply on the original comment
});
if(div.nextSibling.id != "innerid"){ //checks if reply is placed in the correct position
div.nextSibling.appendChild(replycomment); // place new reply
}
else{
  div.appendChild(replycomment); //place new reply
}
};
