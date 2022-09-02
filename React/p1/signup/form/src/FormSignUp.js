import React from 'react'
import useForm from './useForm'

const FormSignUp = () => {
    const {handleChange, values}= useForm()
    return (
        <div className="form-content-right">
        <form  className="form">
            <h1>Get Started With us Today! Create your account by filling out the information</h1>
            <div className="form-inputs">
                <label htmlFor="username" className="form-label">
                    UserName:
                </label>
                <input type="text" className="form-input" name="username" placeholder='Enter your Username' id='username' value={values.username} onChange={handleChange}/>
            </div>
            <div className="form-inputs">
                <label htmlFor="email" className="form-label">
                    Email:
                </label>
                <input type="email" className="form-input" name="email" placeholder='Enter your email' id='email' value={values.email} onChange={handleChange}/>
            </div>
            <div className="form-inputs">
                <label htmlFor="Password" className="form-label">
                    Password:
                </label>
                <input type="password" className="form-input" name="password" placeholder='Enter your password' id='Password' value={values.password} onChange={handleChange}/>
            </div>
            <div className="form-inputs">
                <label htmlFor="Password2" className="form-label">
                    Confirm Password:
                </label>
                <input type="password2" className="form-input" name="password2" placeholder='Confirm your password' id='Password2' value={values.password2} onChange={handleChange}/>
            </div>
            <button className="form-input-btn" type='submit'>
                Sign Up
            </button>
            <span className="form-input-login">
            Already have an account? Login <a href="#">here</a>
            </span>
        </form>
        </div>
    )
}

export default FormSignUp
