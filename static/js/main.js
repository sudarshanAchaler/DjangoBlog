

links= document.getElementsByClassName('nav-link');
for(let x=0; x<links.length; x++){
    var text=links[x].innerHTML;
    if(currentPage==text){
        links[x].classList.add('active')
    }
}

function createComment(body, id){

    var url = '/addComment/';

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
			'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'commentBody': body, 'PostId': id})
    })
    .then((response) => {
        return response.json();
     })

     .then((data)=>{
        location.reload();
        
        
        
         
     })
}


function like(id){
    var url = '/like/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
			'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({ 'PostId': id})
    })
    .then((response) => {
        return response.json();
     })

     .then((data)=>{
        document.getElementById('likesCount').innerHTML=data.likesCount
        if(data.liked=='true'){
            document.getElementById('likeBtn').classList.remove('btn-dark');
            document.getElementById('likeBtn').classList.add('btn-light');
            document.getElementById('likedOrNot').innerHTML='Liked <i class="fas fa-thumbs-up"></i> ';
        }
        else{
            document.getElementById('likeBtn').classList.add('btn-dark');
            document.getElementById('likeBtn').classList.remove('btn-light');
            document.getElementById('likedOrNot').innerHTML='Like <i class="far fa-thumbs-up "></i> ';
        }
        
        
        
         
     })
};

