# Nouvelle version

Ceci est mon nouveau site. Pour l'instant ne prenez pas garde à la suite de cette page. L'ancine site peut-être trouvé [ici](https://old.zonensi.fr).

<iframe src="https://console.basthon.fr/?script=eJxLVLBVMOXlSgJSibxcBUWZeSUaaUqOZYl5JQrJGYl56am5qUBmSqpCWWJOamkRiJWoYKWQaFudWKsA1FadVKukycuVaKtgaIAwwBmnVpA-kAa4VQVFh1cUk2QXRKuSY0kJUHlmfp6OQm4iUCQ1D-ToRIU89dTiEoWCnNJihcMr0xNzFA4vUEhS0gQA4qRNDA" width="100%" height="400"> </iframe>

# Test Heading

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

Documentation sur materials :  [materials reference ](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Test code

``` python linenums="1"  hl_lines="2 3"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```



<iframe src="https://trinket.io/embed/python/3d8d7ce66b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

 :smile:
 
 {--supprime--} et {++insere++} et {== Surligne ==}
 
## Keys

++ctrl++

++alt++

++delete++


## Latex

$$
 \dfrac{3}{4x}
$$

The homomorphism $f$ is injective if and only if its kernel is only the 
singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such 
that $f(a)=f(b)$.

## Admonitions (?)

!!! note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ``` python
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```

    Nunc eu odio eleifend, blandit leo a, volutpat sapien. Phasellus posuere in
    sem ut cursus. Nullam sit amet tincidunt ipsum, sit amet elementum turpis.
    Etiam ipsum quam, mattis in purus vitae, lacinia fermentum enim.


??? Question
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
	
	
!!! Note
On teste l'auto deploiement