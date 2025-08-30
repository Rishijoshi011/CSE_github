
// * 2. Router-Level Middleware

import express from 'express'
// const app = express()
const router = express.Router()


router.use((req, res, next) => {
    console.log(`Router Request method: ${req.method} \nTime:${new Date()}`)
    next()
})

router.get('/', (req, res) => {
    res.send('Birds home page')
})

router.get('/about/:slug', (req, res) => {
    res.send(`This page contains information about ${req.params.slug}`) 
})
    

export default router