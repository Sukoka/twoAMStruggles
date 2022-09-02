import React, {useState} from 'react'
import data from './Data'
import {FaChevronLeft, FaChevronRight, FaQuoteRight} from 'react-icons/fa'

function Review() {
    const [index, setIndex] =useState(1);
    const {name,job,image, text}= data[index];

    const checkNumber= (number) => {
        if (number > data.length-1){
            return 0;
        }if(number < 0){
            return data.length-1;
        }
        return number
    }
    function prevPerson(){
        setIndex((index)=>{
            let newIndex= index-1
            return checkNumber(newIndex);
        })
    }

    function nextPerson(){
        setIndex((index)=>{
            let newIndex= index+1
            return checkNumber(newIndex);
        })
    }
    
    const randomPerson= () => {
        let randomNumber= Math.floor(Math.random() * data.length);
        if (randomNumber=== index){
            randomNumber = index +1
        }
        setIndex(checkNumber(randomNumber))
    }
    return (
        <article className='review'>
            <div className="img-container">
                <img src={image} alt={name} className='person-img'/>
                <span className="quote-icon">
                    <FaQuoteRight/>
                </span>
            </div>
            <h4 className="author">{name}</h4>
            <p className="job">{job}</p>
            <p className="info">{text}</p>
            <div className="button-container">
                <button className='prev-button' onClick={prevPerson}>
                    <FaChevronLeft/>
                </button>
                <button className='next-button' onClick={nextPerson}>
                    <FaChevronRight/>
                </button>
            </div>
                <button className="random-btn" onClick={randomPerson}>Surprise Me Smh</button>
         
        </article>
    )
}
export default Review
