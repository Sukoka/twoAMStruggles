//getting input elements
const inputBox=document.querySelector('.inputfield input')
const addBtn=document.querySelector('.inputfield button')
const todoList=document.querySelector('.to-dolist')
const removeAll=document.querySelector('.footer button')


displayTasks()

inputBox.onkeyup= ()=>{
    let userdata=inputBox.value;
    if(userdata.trim() !=0){
        addBtn.classList.add("active")
    }else{
        addBtn.classList.remove("active")
    }
}

addBtn.onclick= ()=>{
    let userdata=inputBox.value;
    let getLocalStorage= localStorage.getItem('New Todo') 
    if(getLocalStorage==null){
        Arr=[]
    }else{
        Arr= JSON.parse(getLocalStorage)
    }
    Arr.push(userdata)
    localStorage.setItem('New Todo', JSON.stringify(Arr))
    displayTasks()
    addBtn.classList.remove("active")

}
function displayTasks(){
    let getLocalStorage= localStorage.getItem('New Todo') 
    if(getLocalStorage==null){
        Arr=[]
    }else{
        Arr= JSON.parse(getLocalStorage)
    }
    let pendingNum=document.querySelector('.pending')
    pendingNum.textContent= Arr.length
    if(Arr.length >0 ){
        removeAll.classList.add("active")
    }else{
        removeAll.classList.remove("active")
    }
    let newLiTag='';
    Arr.forEach((element, index)=> {
        newLiTag += `<li> ${element} <span onclick="deleteTasks( ${index} )"><i class="fas fa-trash"></i></span></li>`;
    });
    todoList.innerHTML= newLiTag
    inputBox.value="";
}

function deleteTasks(index){
    let getLocalStorage= localStorage.getItem('New Todo')
    Arr= JSON.parse(getLocalStorage)
    Arr.splice(index,1)
    localStorage.setItem('New Todo', JSON.stringify(Arr))
    displayTasks()
}

removeAll.onclick= ()=>{
    Arr=[];
    localStorage.setItem('New Todo', JSON.stringify(Arr))
    displayTasks()

}