import React, { useState, useEffect } from 'react';
import { TextField, Button, Stack, SnackbarContent } from '@mui/material';
import Snackbar from '@mui/material/Snackbar';
import IconButton from '@mui/material/IconButton';
// import CloseIcon from '@mui/icons-material/Close';
import emailjs from '@emailjs/browser';

import  './styles/contactForm.css';

const ContactForm = () => {

  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [email, setEmail] = useState('')
  const [message, setMessage] = useState('')
  const [response, setResponse] = useState('message');
  const [responseStatus, setResponseStatus] = useState(true);
  const [open, setOpen] = React.useState(false);

  const styles = {
    error: {
      background: 'red'
    },
    success: {
      background: 'green'
    }
  };

  const handleClick = () => {
    setOpen(true);
  };

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setOpen(false);
  };

  const action = (
    <React.Fragment>
      <Button color="secondary" size="small" onClick={handleClose}>
        UNDO
      </Button>
      <IconButton
        size="small"
        aria-label="close"
        color="inherit"
        onClick={handleClose}
      >
        {/* <CloseIcon fontSize="small" /> */}
      </IconButton>
    </React.Fragment>
  );


  useEffect(() => {
    emailjs.init("EehQP3OCAFUPh8ECi");
  })

  function handleSubmit(event) {
      event.preventDefault();
      console.log(firstName, lastName, email, message);
      emailjs.send("contact_service", "contact_me_template", {firstName, lastName, email, message}).then(
        (response) => {
          setResponse("An email has been sent, I will contact you soon.");
          setFirstName('');
          setLastName('');
          setEmail('');
          setMessage('');
          setResponseStatus(true);
          setOpen(true);
        },
        (error) => {
          setResponse("The request has failed! Please try again after some time or contact me using linkedIn");
          setResponseStatus(false);
          setOpen(true);
        },
      );
  }

  return (
      <React.Fragment class="contact-form-container">
          <h2 onClick={handleClick}>Contact Me</h2>
          <form onSubmit={handleSubmit}>
              <Stack spacing={2} direction="row" sx={{marginBottom: 4}}>
                  <TextField
                      type="text"
                      variant='outlined'
                      color='secondary'
                      label="First Name"
                      onChange={e => setFirstName(e.target.value)}
                      value={firstName}
                      fullWidth
                      required
                      size='small'
                  />
                  <TextField
                      type="text"
                      variant='outlined'
                      color='secondary'
                      label="Last Name"
                      onChange={e => setLastName(e.target.value)}
                      value={lastName}
                      fullWidth
                      required
                      size='small'
                  />
                  <TextField
                    type="email"
                    variant='outlined'
                    color='secondary'
                    label="Email"
                    onChange={e => setEmail(e.target.value)}
                    value={email}
                    fullWidth
                    required
                    sx={{mb: 4}}
                    size='small'
                />
              </Stack>
              <Stack spacing={2} direction="row" sx={{marginBottom: 4}}>
                <TextField
                    id="outlined-multiline-static"
                    variant='outlined'
                    color='secondary'
                    label="Message"
                    onChange={e => setMessage(e.target.value)}
                    value={message}
                    required
                    multiline
                    fullWidth
                    sx={{mb: 4}}
                    rows={4}
                    size='small'
                />
              </Stack>
              <Button variant="outlined" color="secondary" type="submit">Submit</Button>
          </form>
          <Snackbar
            open={open}
            autoHideDuration={5000}
            onClose={handleClose}
            message={response}
            action={action}
            ContentProps={{
              classes: {
                root: responseStatus ? "success" : "error"
              }
            }}
          >
            <SnackbarContent style={{
                backgroundColor: responseStatus ? 'green' : 'red',
              }}
              message={<span id="client-snackbar">{response}</span>}
            />
          </Snackbar>
      </React.Fragment>
  );
};
// https://www.copycat.dev/blog/material-ui-form/
export default ContactForm;