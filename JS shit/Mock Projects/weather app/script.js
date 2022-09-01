const wrapper= document.querySelector(".wrapper")
inputPart=wrapper.querySelector(".input-part")
infoTxt=inputPart.querySelector(".info-txt")
inputField=inputPart.querySelector("input")
locationBtn=inputPart.querySelector("button")
weatherIcon=document.querySelector(".weather img")
backArrowBtn=wrapper.querySelector("header i")
let api;

inputField.addEventListener("keyup", e=>{
    if(e.key=="Enter" && inputField.value!=""){
        requestAPI(inputField.value)
    }
})



locationBtn.addEventListener("click", e =>{
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(onSuccess, onerror)
    }else{
        alert("Sorry, Your Browser doesn't support geolocation API.")
    }
})

function onSuccess(position){
    const {latitude, longitude}= position.coords;
    api=`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=4d007754555bb40553d4243ae4bdf357`;
    fetchData();
}

function onerror(error){
    infoTxt.innerText=error.message
    infoTxt.classList.add("error")
}
 
function requestAPI(city){
    api=`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=4d007754555bb40553d4243ae4bdf357
`;
    fetchData();
}

function fetchData(){
    infoTxt.innerText='Fetching Weather Details...'
    infoTxt.classList.add("pending")
    fetch(api).then(response=>response.json()).then(result=>weatherDetails(result));
}

function weatherDetails(info){
    if(info.cod=='404'){
        infoTxt.innerText= `${inputField.value} isn't a valid city name`
        infoTxt.classList.replace("pending", "error")
    }else{
        const city=info.name
        const country=info.sys.country
        const {description, id}=info.weather[0]
        const {feels_like, humidity, temp}=info.main

        wrapper.querySelector(".temperature .numb").innerText= Math.floor(temp)
        wrapper.querySelector(".description").innerText= description
        wrapper.querySelector(".location span").innerText= `${city}, ${country}`  
        wrapper.querySelector(".temperature .numb-2").innerText= Math.floor(feels_like)
        wrapper.querySelector(".humidity span").innerText= `${humidity}%`


        if(id==800){
            weatherIcon.src= "/Mock Projects/weather app/Icons/clear.svg"
        }else if(id>=600 || id<=622){
            weatherIcon.src= "/Mock Projects/weather app/Icons/snow.svg"
        }else if(id>=500 || id<=531){
            weatherIcon.src= "/Mock Projects/weather app/Icons/rain.svg"
        }else if(id>=200 || id<=232){
            weatherIcon.src= "/Mock Projects/weather app/Icons/storm.svg"
        }else if(id==721){
            weatherIcon.src="/Mock Projects/weather app/Icons/haze.svg"
        }else if(id>800  || id<=804){
            weatherIcon.src="/Mock Projects/weather app/Icons/cloud.svg"
        };

        infoTxt.innerText=""
        inputField.value=""
        infoTxt.classList.remove("error", "pending")
        wrapper.classList.add("active")
        console.log(info)
    }
    
}

backArrowBtn.addEventListener("click", e =>{
    wrapper.classList.remove("active")
})

