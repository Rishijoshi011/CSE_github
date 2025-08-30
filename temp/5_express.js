// const express = require('express')
import express from 'express'
const app = express()
const port = 3000

app.use(express.static('4_Demo')) // ! this is for static files, standard name for it is public but we are using it as 4_Demo in this folder all files will be accessible

app.get('/', (req, res) => {
    res.send('Hello World! </br> <a href="http://127.0.0.1:3000/about"> got to about page</a>') 
})

app.post('/', (req, res) => {
    res.send('Hello World! this how post method works </br> <a href="http://127.0.0.1:3000/about"> got to about page</a>') 
})

app.get('/about', (req, res) => {
    res.send("This is about page </br> <a href='http://127.0.0.1:3000/'> go to home page</a>")
})

app.get('/index', (req, res) => { 
    res.sendFile('temp.html', {root: './4_Demo'})
})

app.get('/home/:slug', (req, res) => {
    res.send(`Hello: ${req.params.slug}`)
    console.log(req.params)
    console.log(req.query)
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
