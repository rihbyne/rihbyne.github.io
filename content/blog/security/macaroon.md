Title: Macaroon Security
Date: 2018-11-27 20:00
Slug: macaroons-security
Tags: security, encryption, hashing, salting, cryptography, digital signature, tokens,JWT,latex,gradschool
Authors: Rihan Pereira 
Summary: Macaroons, not quite popular in contemporary web development practices, provide a better alternative to web cookies. In short, they are called 'better cookies'

A macaroon is simply a incomprehensible text string at first look but actually holds metadata about authentication and authorization. You can use it to secure user accounts, protect and give controlled access to a resource anywhere in the cloud.

Where did I find out about 'Macaroons' ? This goes back to graduate level security class, fall 2018 where each enrolled student has to do 30 minute presentation on anything confined 
to security. This source [https://paperswelove.org/](https://paperswelove.org/) immediately popped up in mind - which is a community reviewed list of academic CS research papers, categorized into subjects, where I found this [paper](https://github.com/papers-we-love/papers-we-love/blob/master/security/macaroons-cookies-with-contextual-caveats.pdf) and decided to present mainly the motivation, concept and its application. This paper also made me study JSON Web Tokens(JWT) to make a distinction between JWTs and Macaroons, understand cookies at the fundamental level, and evaluate architectures combining multiple methods.

Here's the link [Macaroon Security](../../downloadables/securitytalk.pdf)
