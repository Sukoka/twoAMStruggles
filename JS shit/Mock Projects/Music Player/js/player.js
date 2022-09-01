const wrapper=document.querySelector(".wrapper")
songImg=wrapper.querySelector(".img-area img")
songName=wrapper.querySelector(".song-details .song")
artistName=wrapper.querySelector(".song-details .artist-name")
mainAudio=wrapper.querySelector("#main-audio"),
playPauseBtn=wrapper.querySelector(".control .play-pause"),
prevBtn=wrapper.querySelector(".control #prev"),
nextBtn=wrapper.querySelector(".control #next"),
progressArea=wrapper.querySelector(".progress-area"),
progressBar=wrapper.querySelector(".progress-area .progress-bar"),
musicQueue=wrapper.querySelector(".music-list"),
showMusicQueue=wrapper.querySelector("#queue"),
hideMusicQueue=wrapper.querySelector("#close");

let musicIndex=Math.floor((Math.random()*musicList.length) +1);

window.addEventListener("load", ()=>{
    loadMusic(musicIndex);
    playingNow();
})

function loadMusic(index){
    songName.innerText=musicList[index-1].name;
    artistName.innerText=musicList[index-1].artist;
    songImg.src=`img/${musicList[index-1].img}.jpg`;
    mainAudio.src=`Demo Music/${musicList[index-1].src}.mp3`;
}

function playMusic(){
    wrapper.classList.add("paused")
    playPauseBtn.querySelector("i").innerText= "pause";
    mainAudio.play();
}

function pauseMusic(){
    wrapper.classList.remove("paused")
    playPauseBtn.querySelector("i").innerText= "play_arrow";
    mainAudio.pause();
}

function nextSong(){
    musicIndex++;
    musicIndex > musicList.length ? musicIndex=1 : musicIndex = musicIndex;
    loadMusic(musicIndex);
    playMusic();
    playingNow();
}

function prevSong(){
    musicIndex--;
    musicIndex < 1 ? musicIndex=musicList.length : musicIndex = musicIndex;
    loadMusic(musicIndex);
    playMusic();
    playingNow();
}

playPauseBtn.addEventListener("click", ()=>{
    const isMusicPaused= wrapper.classList.contains("paused");
    isMusicPaused ? pauseMusic() : playMusic()
    playingNow();
});

nextBtn.addEventListener("click", ()=>{
    nextSong();
});

prevBtn.addEventListener("click", ()=>{
    prevSong();
});

mainAudio.addEventListener("timeupdate", (e)=>{
    const currentTime= e.target.currentTime;
    const duration= e.target.duration;
    let progressWidth= (currentTime/duration) * 100;
    progressBar.style.width= `${progressWidth}%`;

    let musicCurrentTime = wrapper.querySelector(".current")
    musicDurationTime = wrapper.querySelector(".duration");

    mainAudio.addEventListener("loadeddata", ()=>{
        let audioDuration = mainAudio.duration;
        let totalMinute= Math.floor(audioDuration / 60);
        let totalSec= Math.floor(audioDuration % 60);
        if(totalSec<10){
            totalSec=`0${totalSec}`;
        }
        musicDurationTime.innerText= `${totalMinute}:${totalSec}`
    })
    let currentMin= Math.floor(currentTime / 60);
    let currentSec= Math.floor(currentTime % 60);
    if(currentSec<10){
    currentSec=`0${currentSec}`;
    }
    musicCurrentTime.innerText= `${currentMin}:${currentSec}`
});
    
progressArea.addEventListener("click", (e)=>{
    let progressWidthval= progressArea.clientWidth;
    let clickedOffSetx= e.offsetX;
    let songDuration= mainAudio.duration;

    mainAudio.currentTime = (clickedOffSetx / progressWidthval) * songDuration;
    playMusic();
})

const repeatBtn=wrapper.querySelector(".control #repeat")
repeatBtn.addEventListener("click", ()=>{
    let getText= repeatBtn.innerText;
    switch(getText){
        case "repeat":
            repeatBtn.innerText= "repeat_one"
            repeatBtn.setAttribute("title", "Song Looped")
            break;
        case "repeat_one":
            repeatBtn.innerText= "shuffle"
            repeatBtn.setAttribute("title", "Shuffle")
            break;
        case "shuffle":
            let randIndex = Math.floor((Math.random() * musicList.length) + 1); 
            do{
            randIndex = Math.floor((Math.random() * allMusic.length) + 1);
            }while(musicIndex == randIndex); 
        musicIndex = randIndex; 
            loadMusic(musicIndex);
            playMusic();
            playingSong();
            break;
    }
});

mainAudio.addEventListener("ended", ()=>{
    let getText= repeatBtn.innerText;
    switch(getText){
        case "repeat":
            nextSong();
            break;
        case "repeat_one":
            mainAudio.currentTime= 0
            loadMusic(index)
            playMusic();
            break;
        case "shuffle":
            let randomIndex= Math.floor((Math.random()* musicList.length)+1);
            do{
                randomIndex= Math.floor((Math.random()* musicList.length)+1);
            }while(musicIndex == randomIndex);
            musicIndex = randomIndex
            loadMusic(musicIndex);
            playMusic();
            playingNow();
            break;
    }
})

showMusicQueue.addEventListener("click", ()=>{
    musicQueue.classList.toggle("show");
});

hideMusicQueue.addEventListener("click", ()=>{
    showMusicQueue.click();
});

const ulTag = wrapper.querySelector("ul");
// let create li tags according to array length for list
for (let i = 0; i < musicList.length; i++) {
  //let's pass the song name, artist from the array
  let liTag = `<li li-index="${i+1}">
                <div class="row">
                  <span>${musicList[i].name}</span>
                  <p>${musicList[i].artist}</p>
                </div>
                <span id="${musicList[i].src}" class="audio-duration"></span>
                <audio class="${musicList[i].src}" src="Demo Music/${musicList[i].src}.mp3"></audio>
              </li>`;
  ulTag.insertAdjacentHTML("beforeend", liTag); 

  let liAudioDuration = ulTag.querySelector(`#${musicList[i].src}`)
  let liAudioTag = ulTag.querySelector(`.${musicList[i].src}`);
  liAudioTag.addEventListener("loadeddata", ()=>{
    let duration = liAudioTag.duration;
    let totalMin = Math.floor(duration / 60);
    let totalSec = Math.floor(duration % 60);
    if(totalSec < 10){ //if sec is less than 10 then add 0 before it
      totalSec = `0${totalSec}`;
    };
    liAudioDuration.innerText = `${totalMin}:${totalSec}`;
    liAudioDuration.setAttribute("t-duration",`${totalMin}:${totalSec}`);
  });
}

const allLiTags=ulTag.querySelectorAll("li");
function playingNow(){
    for(let j=0; j<allLiTags.length; j++){
        let audioTag= allLiTags[j].querySelector(".audio-duration");
        if(allLiTags[j].classList.contains("playing")){
            allLiTags[j].classList.remove("playing");
            let aduration= audioTag.getAttribute("t-duration");
            audioTag.innerText= aduration;
        }

        if(allLiTags[j].getAttribute("li-index") == musicIndex){
            allLiTags[j].classList.add("playing");
            audioTag.innerText="Playing"
        }
        allLiTags[j].setAttribute("onclick", "clicked(this)")
    }
}

function clicked(element){
    let getLiIndex=element.getAttribute("li-index");
    musicIndex= getLiIndex;
    loadMusic(musicIndex);
    playMusic();
    playingNow();
}