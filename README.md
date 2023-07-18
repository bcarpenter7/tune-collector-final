# Tune Collector

[Deployed with fly.io](https://tune-collector.fly.dev/)

## Tunes

The _Tune_ model is used to store information about the _tunes_ that you know how to play. The most important fields are the name of the _tune_, the key it is played in, the tuning required for your instrument, and your personal rating of 1 to 5 stars. It can also store the fiddler known for playing it, the state of origin, and a brief description. All tunes are associated with the _user_ that created it through a related _User_ model.

### Routes

| Method | Path                        | Purpose                                          |                     Note                      |
|--------|-----------------------------|--------------------------------------------------|:---------------------------------------------:|
| GET    | /tunes                      | View all of your _tunes_                         |                  No payload                   |
| GET    | /tunes/\<int:tune_id\>      | View a single _tune_ and its' details            |                  No payload                   |
| GET    | /tunes/create               | View page for adding a _tune_ to your collection |                  No payload                   |
| POST   | /tunes/create               | Adds the new _tune_ to your collection           |          Needs fields for new _tune_          |
| GET    | /tunes/\<int:pk\>/update    | View page for editing your _tune_                |                  No payload                   |
| POST   | /tunes/\<int:pk\>/update    | Edits your _tune_                                |           Updated fields for _tune_           |
| GET    | /tunes/\<int:pk\>/delete    | View page for deleting your _tune_               |                  No payload                   |
| POST   | /tunes/\<int:pk\>/delete    | Deletes your _tune_                              |                  No payload                   |

<br />

## Users

The _User_ model is used to allow anyone to sign up and track their tunes. It requires a unique username and email address, and a strong password. Currently, no email verification is required but could be easily added if needed.

### Routes

> *All _user_ routes start with /account

| Method | Path               | Purpose                                                                         |               Note                |
|--------|--------------------|---------------------------------------------------------------------------------|:---------------------------------:|
| GET    | /register          | View page for registering a _user_                                              |            No payload             |
| POST   | /register          | Adds a new _user_                                                               |    Needs fields for new _user_    |
| GET    | /login             | View page for logging in a _user_                                               |            No payload             |
| POST   | /login             | Logs in a _user_, redirects to home or next page                                | Needs valid username and password |
| GET    | /logout            | Logs out the current _user_, redirects to home page                             |            No payload             |
| GET    | /delete            | View page for deleting current _user_ account                                   |            No payload             |
| POST   | /delete            | "Deletes" current _user_ account, sets _user_ to in-active rather than deleting |            No payload             |
| GET    | /users             | View all other _users_                                                          |            No payload             |
| GET    | /users/\<int:pk\>  | View specific _user_ and their _tunes_                                          |            No payload             |

<br />

## Users

The _User_ model is used to allow anyone to sign up and track their tunes. It requires a unique username and email address, and a strong password. Currently, no verification is required but could be easily added if needed.

### Routes

| Method | Path   | Purpose                                                                  |               Note                |
|--------|--------|--------------------------------------------------------------------------|:---------------------------------:|
| GET    | /      | Home page, with links to register account, login, or view the about page |            No payload             |
| GET    | /about | About page with short description of project and creators                |            No payload             |

<br />

### Screenshots
<img width="300" height="400" alt="Screenshot 2023-07-18 at 1 56 01 PM" src="https://github.com/bcarpenter7/tune-list/assets/126187218/6369ecc1-a446-4881-bed8-de2e1ae29bda">
<img width="300" height="400" alt="Screenshot 2023-07-18 at 1 57 34 PM" src="https://github.com/bcarpenter7/tune-list/assets/126187218/7e961726-e88f-41a8-8f5c-3361b46d7a90">
<img width="300" height="400" alt="Screenshot 2023-07-18 at 1 58 05 PM" src="https://github.com/bcarpenter7/tune-list/assets/126187218/4d930fbd-a25a-43b9-9571-6b760bcb8dda">
<img width="300" height="400" alt="Screenshot 2023-07-18 at 1 58 35 PM" src="https://github.com/bcarpenter7/tune-list/assets/126187218/a2577a42-aec2-42bc-ad15-837b59813954">
<img width="300" height="400" alt="Screenshot 2023-07-18 at 1 59 00 PM" src="https://github.com/bcarpenter7/tune-list/assets/126187218/104c9409-f4b1-43f9-ad45-1d3eb3c0ed95">
<img width="300" height="400" alt="Screenshot 2023-07-18 at 1 59 26 PM" src="https://github.com/bcarpenter7/tune-list/assets/126187218/89796aee-3d9d-4c57-a72a-2a5afbbdcd08">


### Next steps

To complete the _user_ experience, email verification and activation can be added. This will require the ability to send emails using something like AWS Simple Email Service, SendGrid or Mailgun. Adding in the ability to send emails will also give _users_ a good way of resetting their passwords.

Another feature that would improve the usefulness of the site is to enable users to record a short sound clip of their _tune_. This would allow the _user_ to remember the _tune_ they added, or allow other _users_ to hear something that they are not familiar with. This feature will require a good way of storing and accessing audio files. These files will be referenced in the database as a file field of the _Tune_ model.
