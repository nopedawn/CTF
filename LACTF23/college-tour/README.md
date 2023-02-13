## web/college-tour

<details>
  <summary>Description</summary>
  
  > Welcome to UCLA! To explore the #1 public college, we have prepared a scavenger hunt for you to walk all around the beautiful campus. <br> [college-tour.lac.tf](https://college-tour.lac.tf)
    
</details>

Just inspect the sourcecode file on html, css, js then you get 6 part of the flag

On `html` sourcecode

- part-1 `j03_4`
- part-2 `nd_j0`
- part-4 `n3_bR`

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <title>A tour of UCLA</title>
        <link rel="stylesheet" href="index.css">
        <script src="script.js"></script>
    </head>
    <body>
        <h1>A tour of UCLA</h1>
        <button id="dark_mode_button" onclick="dark_mode()">Click me for Light Mode!</button>
        <p>
            After finally setting foot on UCLA's campus, you're excited to explore it. However, the new student advisors have hidden <b>six</b>
            clues in the format lactf{number_text} all across UCLA. To complete the scavenger hunt, you must merge all the parts into one in order. For example, if you find the clues lactf{1_lOsT}, lactf{2__!N_b} (note the repeated underscore), and lactf{3_03LT3r}, the answer is lactf{lOsT_!N_b03LT3r}. Have fun exploring!
        </p>
        <!-- lactf{1_j03_4}-->
        <img src="royce.jpg" alt="lactf{2_nd_j0}" height="400px">
        <iframe src="lactf{4_n3_bR}.pdf" width="100%" height="500px"></iframe>
    </body>
```

On `css` sourcecode

- part-3 `S3phI`

```css
.secret {
    font-family: "lactf{3_S3phI}"
}
```

And `js` sourcecode

- part-5 `U1n_s`
- part-6 `AY_hi`

```javascript
function dark_mode() {
    dark = 1 - dark;
    var element = document.body;
    element.classList.toggle("dark-mode");
    if (dark === 1) {
        document.getElementById("dark_mode_button").textContent = "Click me for Light Mode!";
    }
    else if (dark === 0) {
        document.getElementById("dark_mode_button").textContent = "Click me for Dark Mode!";
    }
    else {
        document.getElementById("dark_mode_button").textContent = "Click me for lactf{6_AY_hi} Mode!";
    }
}

window.addEventListener("load", (event) => {
    document.cookie = "cookie=lactf{5_U1n_s}";
});
```

<details>
  <summary>FLAG</summary>
  
  > `lactf{j03_4nd_j0S3phIn3_bRU1n_sAY_hi}`
    
</details>
