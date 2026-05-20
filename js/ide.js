var tagHdr = "#--- HDR ---#";

var _slate = document.getElementById("ace_palette").dataset.aceDarkMode
var _default = document.getElementById("ace_palette").dataset.aceLightMode

function initAceColor() {
    var bodyStyles = window.getComputedStyle(document.body);
    var primaryColor = bodyStyles.getPropertyValue('--md-primary-fg-color');
    var getRGBChannels = (e) => [parseInt(e.slice(1,3),16), parseInt(e.slice(3,5),16), parseInt(e.slice(5,7),16)]
    document.documentElement.style.setProperty('--main-color', getRGBChannels(primaryColor));  
}

function toggleComments(editor) {
    let code = editor.getSession().getValue()  
    let commentedCode = []
    let inTestsBlock = false
    for (let line of code.split('\n')) {
        if (inTestsBlock == true && line !== "") {
            line.slice(0,2) === '# ' ? commentedCode.push(`${line.slice(2)}`)
                                        : commentedCode.push(`# ${line}`)
        }
        else commentedCode.push(`${line}`)
        if (/#(\s*)Test(s?)[^\n]*/i.test(line)) inTestsBlock = true;
    }
    editor.getSession().setValue(commentedCode.join('\n'))
}

function createTheme() { 
    initAceColor()
    var bodyStyles = window.getComputedStyle(document.body);
    var primaryColor = bodyStyles.getPropertyValue('--md-primary-fg-color');
    var getRGBChannels = (e) => [parseInt(e.slice(1,3),16), parseInt(e.slice(3,5),16), parseInt(e.slice(5,7),16)]
    document.documentElement.style.setProperty('--main-color', getRGBChannels(primaryColor));
    
    let customLightTheme = _default.split('|')[1] === undefined ? 'default' : _default.split('|')[1]
    let customDarkTheme = _slate.split('|')[1] === undefined ? 'slate' : _slate.split('|')[1]
    // Correspondance between the custom and the classic palettes
    let customTheme =  {[customLightTheme] : 'default', [customDarkTheme]: 'slate'}
    // Get ACE style
    var ace_style = {"default": _default.split('|')[0] , "slate": _slate.split('|')[0]}
    // automatically load current palette
    let curPalette = __md_get("__palette") !== null ?   // first load tester
                __md_get("__palette").color["scheme"] :
                customLightTheme
    return  "ace/theme/" + ace_style[customTheme[curPalette]]
};

$('[id^=editor_]').each(function() {
    let number = this.id.split('_').pop();
    let url_pyfile = $('#content_'+this.id).text()  // Extracting url from the div before Ace layer

    if (url_pyfile.includes(tagHdr)) { // test if a header code is present
        splitHdrPyFile = url_pyfile.match(new RegExp(tagHdr + "(.*)" + tagHdr + "(.*)"));
        if (splitHdrPyFile === null) { var pyFile = `Missing ${tagHdr} tag. Please check !\n\n` + url_pyfile } 
        else {
            hdrFile = splitHdrPyFile[1];
            var pyFile = splitHdrPyFile[2];
            newline = 'bksl-nl';
            while(pyFile.startsWith(newline)) { pyFile = pyFile.substring(newline.length); }
        }
    } else {
        var pyFile = url_pyfile;
    }

    pyFile = pyFile.replace(/bksl-nl/g, "\n").replace(/py-und/g, "_").replace(/py-str/g, "*")

    let idEditor = "editor_" + number
    function createACE(idEditor){
        ace.require("ace/ext/language_tools");
        var editor = ace.edit(idEditor, {
            theme: createTheme(),
            mode: "ace/mode/python",
            autoScrollEditorIntoView: true,
            maxLines: 30,
            minLines: 6,
            tabSize: 4,
            printMargin: false   // hide ugly margins...
        });
        editor.setOptions({
            // https://github.com/ajaxorg/ace/blob/092b70c9e35f1b7aeb927925d89cb0264480d409/lib/ace/autocomplete.js#L545
            enableBasicAutocompletion: true,
            enableSnippets: true,
            enableLiveAutocompletion: false,
        });
        // editor.commands.bindKey({win: 'Tab', mac: 'Tab'}, 'startAutocomplete')
        editor.commands.bindKey({win: 'Alt-Tab', mac: 'Alt-Tab'}, 'startAutocomplete')
        editor.getSession().setValue(pyFile)  
        editor.commands.addCommand({
            name: 'commentTests',
            bindKey: {win: "Ctrl-I", mac: "Cmd-I"},
            exec: (editor) => toggleComments(editor)
        });
    }
    window.IDE_ready = createACE(idEditor) // Creating Ace Editor #idEditor
    
    // console.log(editor.getSession().getValue())
    // console.log(/#(\s*)Test(s?)[^\n]*/i.test(editor.getSession().getValue()))
    
    var nChange = 0;
    let editor = ace.edit(idEditor);
    if (/#(\s*)Test(s?)[^\n]*/i.test(editor.getSession().getValue()) == false) {
        let commentButton = document.getElementById('comment_' + idEditor)
        commentButton.parentNode.removeChild(commentButton)
    } else {
        document.getElementById('comment_'+idEditor).addEventListener('click', () => toggleComments(editor))
    }

    editor.addEventListener('input', function() {
    if (nChange % 25 == 0) localStorage.setItem(idEditor, editor.getSession().getValue())
    nChange += 1;
    });

    let storedCode = localStorage.getItem(idEditor);
    if (storedCode !== null) ace.edit(idEditor).getSession().setValue(storedCode)

    // Create 6 empty lines
    if (url_pyfile === '') ace.edit(idEditor).getSession().setValue('\n'.repeat(6));  

    // A correction Element always exists (can be void)
    prevNode = document.getElementById("corr_content_" + idEditor)
    var key = prevNode.dataset.strudel
    var workingNode = prevNode
    var remNode = document.createElement("div");

    console.log('la1', idEditor, key)
    console.log('la2', prevNode)
    console.log('la3', prevNode.innerHTML)

    // console.log('la4', prevNode.innerHTML)
    if (prevNode.innerHTML !== '' || key !== "") {
        // soit y a pas de correction, soit la clé SHA256 n'est pas vide
    if (prevNode.parentNode.tagName === 'P') {
        // REM file on top level
        workingNode = prevNode.parentNode.nextElementSibling //'<strong>A</strong>'
        // console.log('bef', idEditor)
        // console.log(workingNode.innerHTML) 
        // console.log(workingNode.nextElementSibling.innerHTML) 
        // console.log(prevNode.parentNode.nextElementSibling, workingNode.innerHTML)
        // if (workingNode.nex)

        if (workingNode.innerHTML.includes('<strong>A</strong>') && workingNode.nextElementSibling.innerHTML.includes('<strong>Z</strong>')) {
            remNode.innerHTML = 'Pas de remarque particulière.';
            workingNode.nextElementSibling.remove()
            workingNode.remove()
        }
        else 
        {
        workingNode.remove()
        workingNode = prevNode.parentNode.nextElementSibling
        // console.log(prevNode.parentNode)

        var tableElements = [];
        while (!workingNode.innerHTML.includes('<strong>Z</strong>')) {
            tableElements.push(workingNode)
            workingNode = workingNode.nextElementSibling;
        }
        workingNode.remove()

        for (let i = 0; i < tableElements.length; i++) remNode.append(tableElements[i])
        }

    } else {
        // Search for the rem DIV.
        workingNode = workingNode.nextElementSibling
        // console.log(prevNode, workingNode)
        // If workingNode is a <p> (admonition), we continue
        // else, we are outside an admonition
        if (workingNode !== null) workingNode = workingNode.nextElementSibling

        // No remark file. Creates standard sentence.
        if (workingNode === null) remNode.innerHTML = 'Pas de remarque particulière.';
        else 
        {

        var tableElements = [];
        while (workingNode !== null) {
            tableElements.push(workingNode);
            workingNode = workingNode.nextElementSibling;
        }

        for (let i = 0; i < tableElements.length; i++) remNode.append(tableElements[i])
        
        }
    }

    if (key != "")  
    /* another possible condition is this : 
    !remNode.innerHTML.includes('<h1'))  */
    {  
        remNode = document.createElement("div");
        remNode.innerHTML = `Vous trouverez une analyse détaillée de la solution <a href = "../${md5('e-nsi+' + key)}/exo_REM/" target="_blank"> en cliquant ici </a>`
    }

    prevNode.insertAdjacentElement('afterend', remNode)
    remNode.setAttribute("id", "rem_content_" + idEditor);
    document.getElementById("rem_content_" + idEditor).style.display = "none"
    } else {
        console.log('on est là ICIIII!')
        workingNode = prevNode.parentNode.nextElementSibling
        if (workingNode.innerHTML.includes('<strong>A</strong>') && workingNode.nextElementSibling.innerHTML.includes('<strong>Z</strong>')) {
            workingNode.nextElementSibling.remove()
            workingNode.remove()
        }
    }

}

);

// Javascript to upload file from customized buttons
$('[id^=input_editor_]').each(function() {
    let number = this.id.split('_').pop();
    let idEditor = "editor_" + number
    document.getElementById('input_'+idEditor).addEventListener('change', function(e) {readFile(e, idEditor)}, false);
});

function readFile(evt, idEditor) {
    let file = evt.target.files[0];
    let reader = new FileReader();
    var editor = ace.edit(idEditor);
    reader.onload = function(event) {
        editor.getSession().setValue(event.target.result);
    }
    reader.readAsText(file)
};

// Following blocks paint the IDE according to the mkdocs light/dark mode 
function paintACE() {
    let theme = createTheme()
    for (let editeur of document.querySelectorAll('div[id^="editor_"], div[id^="corr_editor_"]')) {
        let editor = ace.edit(editeur.id);
        editor.setTheme(theme);
        editor.getSession().setMode("ace/mode/python"); // USEFUL ????
    };
}

window.addEventListener('DOMContentLoaded', () => paintACE());

document.querySelector('[data-md-color-scheme]').addEventListener('change', () => paintACE())

// turn off copy paste of code... A bit aggressive but necessary
$(".highlight").bind('copy paste',function(e) { e.preventDefault(); return false; });

// $('[id^=qcm_]').each(function() {
//     console.log(this.id)
//     let number = this.id.split('_').pop();
//     // let url_pyfile = $('#qcm_'+this.id) // Extracting url from the div before Ace layer
//     console.log(number)
// });

// document.querySelector('#qcm_0').addEventListener('click', ()=> {console.log('lick')})

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('pre code.qcm').forEach((el) => {
      hljs.highlightElement(el);
    });
  });

function randomizeQCM(el) {
    let qcmAns = el.childNodes;
    if (el.dataset.shuffle == 1) {
        for (let i = qcmAns.length; i >= 0; i--) el.appendChild(qcmAns[Math.floor(Math.random() * i)])
    }
}

document.querySelectorAll("[id^=qcm_]").forEach((el) => {
    randomizeQCM(el)

    for (let element of el.children) {
        element.addEventListener('click', () => {
        // element.firstChild.disabled = true
        if (!element.firstChild.disabled) {
            if (!maxAnswerReached(el)) element.firstChild.checked = !(element.firstChild.checked)
            else if (element.firstChild.checked) element.firstChild.checked = !(element.firstChild.checked)
    }})
    }
});

function nTotalAnswers(el) {
    let somme = 0;
    for (let question of el.children) {
        if (question.className == "wrapper_qcm") {
            somme += parseInt(question.dataset.nCorrect)
            console.log(somme) 
        }
    }
    return somme
}

function maxAnswerReached(el) {
    let somme = 0;
    for (let answer of el.children) if (answer.firstChild.checked) somme += 1;
    return somme >= parseInt(el.dataset.nCorrect)
}

function nRightAnswers(el) {
    let somme = 0;
    for (let question of el.children) {
        if (question.className == "wrapper_qcm") {
            for (let answer of question.children) {
                if (answer.firstChild.checked) {
                    if (answer.firstChild.classList.contains("correct")) somme += 1;
                    answer.firstChild.classList.add("reveal");
                }
                answer.firstChild.disabled = true;
            }
        }
    }
    return somme
}



// document.getElementById("valider").addEventListener("click", () => {
//     let elScore = document.getElementById("score");
//     let totalScore = nTotalAnswers(elScore.parentElement);
//     let studentScore = nRightAnswers(elScore.parentElement);
//     if (studentScore/totalScore > 0.5) {
//         elScore.innerHTML = `Bon travail ! Score : ${studentScore} / ${totalScore}`;
//     } else {
//         elScore.innerHTML = `Cours à reprendre. Score : ${studentScore} / ${totalScore}`;
//     }
// })

// document.getElementById("recharger").addEventListener("click", () => {
//     let elScore = document.getElementById("score")
//     elScore.innerHTML = "";
//     for (let question of elScore.parentElement.children) {
//         if (question.className == "wrapper_qcm") {
//             for (let answer of question.children) {
//                 answer.firstChild.classList.remove("reveal")
//                 answer.firstChild.disabled = false;
//                 answer.firstChild.checked = false;
//             }
//             randomizeQCM(question)
//         }
//     }
// })

document.querySelectorAll("[id^=valider_]").forEach((el) => {
    let number = el.id.split('_').pop();
    console.log(number)
    el.addEventListener("click", () => {
        let elScore = document.getElementById(`score_${number}`);
        let totalScore = nTotalAnswers(elScore.parentElement);
        let studentScore = nRightAnswers(elScore.parentElement);
        if (studentScore/totalScore > 0.5) {
            elScore.innerHTML = `Bon travail ! Score : ${studentScore} / ${totalScore}`;
        } else {
            elScore.innerHTML = `Cours à reprendre. Score : ${studentScore} / ${totalScore}`;
        }
        // let blabla = document.createElement('DIV');
        // blabla.setAttribute("id", "Div1");
        // let truc = document.createTextNode('$\\frac{1}{2}$')
        // blabla.appendChild(truc)
        // var curre = document.getElementById(`score_${number}`).parentElement
        // curre.insertAdjacentElement("afterend", blabla)
        // // window.MathJax.
        // window.MathJax.startup.document.clear();
        // window.MathJax.startup.document.updateDocument();
})})

function normalize_var(html_attribute) {return html_attribute.slice(3).toLowerCase()}

function create_dictionnary(dataset) {
    let var_dictionnary = {};
    for (let html_attr in dataset) {
        if (html_attr.startsWith("var")) {
            var_name = normalize_var(html_attr) // pas de majuscule dans les noms de variables.
            var_dictionnary[var_name] = dataset[html_attr].startsWith("[") ? JSON.parse(dataset[html_attr]) : JSON.parse("["+dataset[html_attr]+"]")
        }
    }
    return var_dictionnary
}

let pick_rnd_value = (list_values) => list_values[Math.floor(Math.random()*list_values.length)]

function pick_rnd_values(var_dict) { 
    let picked_var_dict = {}
    for (let var_name in var_dict) picked_var_dict[var_name] = pick_rnd_value(var_dict[var_name])
    return picked_var_dict
}

function process_rnd_formula(htmlElement, var_dict) {
    if (var_dict !== {}) { // there is variable parts
        if (MathJax.startup.document.getMathItemsWithin(htmlElement)[0]) {  // there is a math formula
            // console.log(htmlElement, htmlElement.htmlFor)
            let formula = MathJax.startup.document.getMathItemsWithin(htmlElement)[0].math;
            for (let var_name in var_dict) {
                if (formula.includes(`{${var_name}}`)) sessionStorage.setItem(`${htmlElement.htmlFor}`, formula);
                else formula = sessionStorage.getItem(`${htmlElement.htmlFor}`)
            }
            for (let var_name in var_dict) formula = formula.replace(`{${var_name}}`, var_dict[var_name])
            console.log(formula)
            htmlElement.innerHTML = `\\(${formula}\\)`
        }
    }
}

document.querySelectorAll("[id^=recharger_]").forEach((el) => {
    let number = el.id.split('_').pop();
    el.addEventListener("click", () => {
        let elScore = document.getElementById(`score_${number}`)
        elScore.innerHTML = "";
        for (let question of elScore.parentElement.children) {
            if (question.className == "wrapper_qcm") {
                let var_dictionnary = create_dictionnary(question.dataset)
                var picked_var_dict = pick_rnd_values(var_dictionnary)

                for (let answer of question.children) {
                    answer.firstChild.classList.remove("reveal")
                    answer.firstChild.disabled = false;
                    answer.firstChild.checked = false;
                    // answer.lastChild.innerHTML = 
                    process_rnd_formula(answer.lastChild, picked_var_dict)
                }
                MathJax.typeset()
                
                // for (let i in var_dictionnary['p']) console.log(i)
                randomizeQCM(question)
            }
        }
    })})



// const node = document.getElementsByClassName('arithmatex');
// console.log("arithmatex", node)
// window.MathJax.typesetClear(node[2]);
// window.MathJax.startup.document.clear();
// window.MathJax.startup.document.updateDocument();

// // node.innerHTML = new_html;
// // MathJax.typesetPromise([node]).then(() => {
// //   // the new content is has been typeset
// // });