import zlib, base64

exec(
    zlib.decompress(
        base64.b64decode(
            "eJytVVtr2zAUfvevEH2yqWfa14AeypKGlXlNL5SCMUZO5FTMlhRZbpZu++87ujiOm3QwGJRU56pzvu8cuVKiQUxTpYWoW8QaKZRGrK3ZkgaVMS4bmXSaDcbPgmvCOFUPVAcrWqGlaGSnaVGLJamLiqlWh/a3jUktX0g0CVCFnSZAEltlgKb4MFMYBUirHbiiBZbJl3YmW1YLHiD6Y0mldoZrUrc0QKxCC6OYJi3VBXWeJgMFszFUQqE5YhxJI6EUV9k8N6dp0skV0TRMIyNCIi40SpOlK6Xtk9kwVCpKvsOpT3t8oaK6UxxNR0C4VsO5a/zn7wDN8KPqoHBTV2nqmieAecM49GPrzcp8DEcZOW/tvLngj+MAnR/ht31hNUUzY5/1UNkkty7JQolVt9RMcJsDPePb5CuttDlLON+z9YsVrgCvZ4uXpwQ6B5W0qoGPXntUCEI3+ORUxNJaZ7/wNHkhalV4Nm569dWR2iNcjREWdS22AHHssB6P2GaEObXSX7DcnMJyk82TVhOlH3ZNKep3DvNkdnv9PxG/xxuPuIlmcbszCSjvGqoMEjJygMPAtjvYjm9DD86A7iBDu8udsKcN8pWYZjJm3nLI3oHxA7rcQxCCx/llDHfSKHKRQNVdv0pV6ZVQXFV+sErjkPuB2I0ltuxYvSokUS3j60KTsqZ7cmPP9pjkCo5OH8B+9xSTk7g/Y9LDvoBjj7oJoCagyhb5ZDTuafYc0zwhUlK+Ckn0fvCdHWfEwGr6hgynOx8uMTvlogd6Tt0z5ujwJg9ZaiFrqBYrUUhFVwxafRUFF4Wiyw4wfBWAXooNYx5Ef3aIWcHCyQY8xYAnNJTCRwAZt4lvkB0qTODRa+cdxdhR4FNLa5xT/BHrUCc42CbDrZ38J5zZnYvHWwmWpsEX8O8NZ0ZyC2kW396+xk+JFNK9SQRvs6bJ/bu/hi0ar5BRYkwm+2EGyV7aT3D/OUAHXwRkKjjHl8E7rVSM6/BsppRQCboq4csJPSZJcuaXxXNpgApGocNwLHCarWOSZxd+ee3bYGZJEb6mYU15uHDTHH26jO1f1Ff11A+V98hY7m9+21tOjNs/1u2lt/1sNsEfuhaMXQ=="
        )
    )
)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

deprecated_metodo_predictivo_no_recursivo = metodo_predictivo_no_recursivo


def metodo_predictivo_no_recursivo(G, M=None, firsts=None, follows=None):
    parser = deprecated_metodo_predictivo_no_recursivo(G, M, firsts, follows)

    def updated(tokens):
        return parser([t.token_type for t in tokens])

    return updated
