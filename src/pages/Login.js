import React, { useState, useEffect } from "react";
import {
    Button,
    Form,
    Grid,
    Header,
    Image,
    Message,
    Segment,
} from "semantic-ui-react";
import {Redirect} from 'react-router-dom'
import url from '../url'

function Login() {
    const [user, setUser] = useState({
        username: "",
        password: "",
    });

    const [error, setError] = useState({
        status: false,
        msg: "",
    });

    const [redirect, setRedirect] = useState(false);
    const [subRedirect, setSubRedirect] = useState(false);


    useEffect(() => {
        document.body.classList.add("Platform");
    }, []);

    const handleChange = (e) => {
        setUser({
            ...user,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        console.log(user);
        fetch(`${url}api/token/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
                try{
                    if (data.access){
                        document.cookie = "access=" + data.access
                        const token = data.access
                        console.log(url)
                        fetch(`${url}portal/getuserlevel`,{
                            headers:{
                                Authorization: `Bearer ${token}`,
                            },
                        })
                        .then((res) => res.json())
                        .then(data => {
                            console.log(data)
                            document.cookie = "level=" + data.level
                            if(data.level === 2)
                                setRedirect(true);
                            else if(data.level === 1)
                                setSubRedirect(true)
                        })
                        .catch(e => console.log(e))
                    } 
                    else
                        setError({
                            status: true,
                            msg: "Wrong username or Password",
                        });
                }
                catch{
                    setError({
                        status: true,
                        msg: "Wrong username or Password",
                    });
                }
                
            });
    };

    return (
        <div>
        {redirect &&  <Redirect push to="/dashboard" />}
        {subRedirect &&  <Redirect push to="/subdashboard" />}
            <Grid
                textAlign="center"
                style={{ height: "100vh" }}
                verticalAlign="middle"
            >
                <Grid.Column style={{ maxWidth: 450 }}>
                    <Header as="h2" color="teal" textAlign="center">
                        <Image src="https://react.semantic-ui.com/logo.png" />{" "}
                        Log-in to your account
                    </Header>
                    <Form size="large" onSubmit={handleSubmit}>
                        <Segment stacked>
                            <Form.Input
                                fluid
                                icon="user"
                                iconPosition="left"
                                placeholder="Username"
                                name="username"
                                value={user.username}
                                onChange={handleChange}
                            />
                            <Form.Input
                                fluid
                                icon="lock"
                                iconPosition="left"
                                placeholder="Password"
                                type="password"
                                name="password"
                                value={user.password}
                                onChange={handleChange}
                            />
                            {error.status && (
                                <Message negative>
                                    <Message.Header>{error.msg}</Message.Header>
                                </Message>
                            )}
                            <Button
                                color="teal"
                                fluid
                                size="large"
                                type="submit"
                            >
                                Login
                            </Button>
                        </Segment>
                    </Form>
                </Grid.Column>
            </Grid>
        </div>
    );
}

export default Login;
