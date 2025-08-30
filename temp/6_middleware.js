
// ! Types of Middleware

/* 
    ! 1. Application-Level Middleware
    ! 2. Router-Level Middleware
    ! 3. Error-Handling Middleware
    ! 4. Built-in Middleware
    ! 5. Third-Party Middleware

*/ 

import express from 'express'
const app = express()
const port = 3000

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})


// * 1. Application-Level Middleware

// app.use((req, res, next) => {
//     console.log(`Request method: ${req.method} \nTime:${new Date()}`)
//     next()
// })

app.get('/',(req, res) =>{
    res.send('Home Page')
    console.log('Home Page')
})

// * 2. Router-Level Middleware

import router from './Routes/routes_birds.js'

app.use('/birds', router) 

// * 3. Error-Handling Middleware

app.get('/err', (req, res) => {
    throw new Error('BROKEN') // Express will catch this on its own.
    res.send('This will not run')
})

app.use((err, req, res, next) => {
    err.status = 500;
    res.status(err.status).send(err.message);
    console.error(err.stack)
})



