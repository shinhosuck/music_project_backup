// BASE.HTML
// navbar
const barBtn = document.querySelector(".bar-btn");
const navItems = document.querySelector(".nav-items")

// show or hide navigation bar items
barBtn.addEventListener("click", function(){
    if(navItems.classList.contains("nav-items")){
        navItems.classList.remove("nav-items")
        navItems.classList.add("show-nav-items")
    }else{
        navItems.classList.add("nav-items")
        navItems.classList.remove("show-nav-items")
    }
})
window.addEventListener("resize", function(){
    if(window.innerWidth > 740){
        navItems.classList.remove("show-nav-items")
        navItems.classList.add("nav-items")
    }
})
// end navbar
// END BASE.HTML

// HOME.HTML
const containerItems = document.querySelectorAll(".container-items");
const sideWindowPlayLink = document.querySelectorAll(".side-window-play-link")
const playBtns = document.querySelectorAll(".play-btn")

containerItems.forEach(function(item){
	item.addEventListener("mouseover", function(event){
		const child_elements = event.currentTarget.children
		for(i=0; i < child_elements.length; i++){
			if(child_elements[i].classList.contains("hide-btn")){
				child_elements[i].classList.remove("hide-btn");
				child_elements[i].classList.add("show-btn")
			}
		}
	})
})
containerItems.forEach(function(item){
	item.addEventListener("mouseleave", function(event){
		const child_elements = event.currentTarget.children
		for(i=0; i < child_elements.length; i++){
			if(child_elements[i].classList.contains("show-btn")){
				child_elements[i].classList.remove("show-btn")
				child_elements[i].classList.add("hide-btn");
			}
		}
	})
})
// window.addEventListener("resize", function(){
// 	playBtns.forEach( function(btn) {
// 		if(window.innerWidth < 700) {
// 			btn.classList.add("show-btn")
// 			btn.classList.remove("hide-btn")
// 			containerItems.forEach(function(item) {
// 			item.removeEventListener("mouserover", this.item)
// 			item.removeEventListener("mouseleave", this.item)
// 		});
// 		}
// 		else if(window.innerWidth > 700) {
// 			btn.classList.remove("show-btn")
// 			btn.classList.add("hide-btn")
// 			containerItems.forEach(function(item) {
// 			item.removeEventListener("mouserover", this)
// 			item.removeEventListener("mouseleave", this)
// 		});
// 		}
// 	});
// })
// side window
sideWindowPlayLink.forEach(function(item){
	item.addEventListener("mouseenter", function(event){
		const child_elements = event.currentTarget.children
		for(i=0; i < child_elements.length; i++){
			if(child_elements[i].classList.contains("side-window-hide-btn")){
				child_elements[i].classList.remove("side-window-hide-btn");
				child_elements[i].classList.add("side-window-show-btn")
			}
		}
	})
})
sideWindowPlayLink.forEach(function(item){
	item.addEventListener("mouseleave", function(event){
		const child_elements = event.currentTarget.children
		for(i=0; i < child_elements.length; i++){
			if(child_elements[i].classList.contains("side-window-show-btn")){
				child_elements[i].classList.remove("side-window-show-btn")
				child_elements[i].classList.add("side-window-hide-btn");
			}
		}
	})
})

// END HOME.HTML

// MY_ALBUM.HTML
const myAlbumContainerItems = document.querySelectorAll(".my-album-container-items");
const profileBtnContainer = document.querySelector(".profile-btn-container")
const myProfile = document.querySelector(".profile-hide");
const btnUp = document.querySelector(".btn-up-show");
const btnDown = document.querySelector(".btn-down-hide");

myAlbumContainerItems.forEach(function(item){
	item.addEventListener("mouseenter", function(event){
		const child_elements = event.currentTarget.children
		for(i=0; i < child_elements.length; i++){
			if(child_elements[i].classList.contains("my-album-hide-btn")){
				child_elements[i].classList.remove("my-album-hide-btn");
				child_elements[i].classList.add("my-album-show-btn")
			}
		}
	})
})
myAlbumContainerItems.forEach(function(item){
	item.addEventListener("mouseleave", function(event){
		const child_elements = event.currentTarget.children
		for(i=0; i < child_elements.length; i++){
			if(child_elements[i].classList.contains("my-album-show-btn")){
				child_elements[i].classList.remove("my-album-show-btn")
				child_elements[i].classList.add("my-album-hide-btn");
			}
		}
	})
})
// END MY_ALBUM.HTML

// PLAY_ALBUM.HTML
let songContainer = document.querySelector("#song-container")
let song = document.querySelectorAll(".song")


const playBtn = document.querySelector("#play")
const forwardBtn = document.querySelector("#forward")
const backBtn = document.querySelector("#back")
const pauseBtn = document.querySelector("#pause")

const progressBar = document.querySelector("#progress");
const songDuration = document.querySelectorAll(".song-duration")
const songLength = document.querySelectorAll("#song-length")
const playerSongContainer = document.querySelectorAll(".player-song-container")

let songTitle = document.querySelectorAll(".song-title")
let convertSongTitle = [...songTitle]
const maxDuration = document.querySelector(".max-duration")
const initial = document.querySelector(".initial")

let index = 0

let song_list_length = song.length-1

// audio duration/length
for(i=0; i < songLength.length; i++){
	songDuration[i].textContent = songLength[i].textContent
}

// audio progress bar
song.forEach(function(s){
	s.addEventListener("timeupdate", function(){
		progressBar.value = s.currentTime / s.duration;
	})
})

// song max duration
maxDuration.textContent = songLength[index].textContent

// initial song background and text color
convertSongTitle.forEach(function(title){
	maxDuration.textContent = songLength[index].textContent
	if(convertSongTitle.indexOf(title) == index){
		title.style.color = "white"
		title.parentElement.style.background = "rgb(81, 81, 81)"
	}
})

// plays next song automatically and changes the song title background color
song.forEach(function(item){
	item.addEventListener("ended", function(event){
		index++
		if(event.currentTarget.paused && index > song_list_length){
			index = 0
			song[index].play()
			maxDuration.style.display = "block"
			initial.style.display = "block"
		}
		else{
			song[index].play()
		}
		maxDuration.textContent = songLength[index].textContent
		convertSongTitle.forEach(function(title){
			// title.style.color = "rgb(255, 255, 255)"
			// title.parentElement.style.background = "rgb(41, 41, 41)"

		if(convertSongTitle.indexOf(title) == index){
			title.style.color = "rgb(255, 255, 255)"
			title.parentElement.style.background = "rgb(81, 81, 81)"
		}
	})
	})
})

// play button
playBtn.addEventListener("click", function(){
	if(song[index].paused){
		song[index].play()
		playBtn.style.display = "none"
		pauseBtn.style.display = "block"
	}
	maxDuration.textContent = songLength[index].textContent
})

// pause button
pauseBtn.addEventListener("click", function(){
	if(!song[index].paused){
		song[index].pause()
		playBtn.style.display = "block"
		pauseBtn.style.display = "none"
	}
})
// forward button
forwardBtn.addEventListener("click", function(){
	if(song[index].duration > 0 && !song[index].paused){
		song[index].pause()
		index++
		if(index > song_list_length){
			index = 0
		}
		song[index].currentTime = 0
		song[index].play()
		maxDuration.textContent = songLength[index].textContent
	}
	else if(song[index].paused){
		index++
		if(index > song_list_length){
			index = 0
		}
		song[index].currentTime = 0
		song[index].play()
		pauseBtn.style.display = "block"
		playBtn.style.display = "none"
		maxDuration.textContent = songLength[index].textContent
	}
	convertSongTitle.forEach(function(title){
		title.style.color = "rgb(255, 255, 255)"
		title.parentElement.style.background = "rgb(41, 41, 41)"

		if(convertSongTitle.indexOf(title) == index){
			title.style.color = "rgb(255, 255, 255)"
			title.parentElement.style.background = "rgb(81, 81, 81)"
		}
	})
})

// back button
backBtn.addEventListener("click", function(){
	if(song[index].duration > 0 && !song[index].paused){
		song[index].pause()
		index--
		if(index == -1){
			index = song_list_length
		}
		song[index].currentTime = 0
		song[index].play()
		maxDuration.textContent = songLength[index].textContent
	}
	else if(song[index].paused){
		index--
		if(index == -1){
			index = song_list_length
		}
		song[index].currentTime = 0
		song[index].play()
		pauseBtn.style.display = "block"
		playBtn.style.display = "none"
		maxDuration.textContent = songLength[index].textContent
	}
	convertSongTitle.forEach(function(title){
		title.style.color = "rgb(255, 255, 255)"
		title.parentElement.style.background = "rgb(41, 41, 41)"

		if(convertSongTitle.indexOf(title) == index){
			title.style.color = "rgb(255, 255, 255)"
			title.parentElement.style.background = "rgb(81, 81, 81)"
		}
	})
})
// END PLAY_ALBUM.HTML
