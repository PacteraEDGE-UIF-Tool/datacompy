import React, {useEffect, ReactElement} from "react"
import {
  withStreamlitConnection,
  Streamlit,
  ComponentProps,
} from "streamlit-component-lib"


import Card from '@material-ui/core/Card'
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'
import Typography from '@material-ui/core/Typography'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'

import styles from './style.module.scss'
import {Formik, Form, Field} from 'formik'

function TestComponent(args){
    return(
            <Form>
            </Form>
          )
      
    }

export default withStreamlitConnection(TestComponent)