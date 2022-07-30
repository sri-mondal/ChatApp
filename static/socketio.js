const socket = io();
document.getElementById("send-btn").onclick = btnclicked;
const posts = document.getElementById("posts")
function btnclicked(){
    const username = document.getElementById("username").value;
    const content = document.getElementById("content").value;
    socket.send([username, content])
}
socket.on('message',createpost);
function createpost(data){
    const card = document.createElement('div');
    const cardheader = document.createElement('h4');
    const cardcontent = document.createElement('p');
    cardheader.textContent = data[0]
    cardheader.classList.add('card-header')
    cardcontent.classList.add('card-body')
    card.classList.add('card','mb-2')
    cardcontent.textContent = data[1]
    card.append(cardheader, cardcontent)
    posts.prepend(card)
}

