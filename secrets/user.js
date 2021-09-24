db.createUser(
    {
        user: "admin",
        pwd: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVmlzd2FuYXRoIiwiYmRheSI6IjA3MDY5MSJ9.pJON0_SkORR6MLNGHPLKZIEjcZMiUZt3FutPNs16GOk",
        roles:[
            {
                role: "readWrite",
                db: "parks"
            }
        ]
    }
);
