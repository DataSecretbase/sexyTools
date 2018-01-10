var xmlHttp;
function showUser()
{
    xmlHttp=GetXmlHttpObject();
    if (xmlHttp==null)
    {
        console.log(xmlHttp.responseJson)
            return;

    }
    var url="functions/getshanbei_voc.php?word="+document.getElementById('voc').value;
    console.log(url);
    xmlHttp.onreadystatechange=stateChanged;
    xmlHttp.open("GET",url,true);
    xmlHttp.send(null);

}
var jsoo;
function stateChanged()
{
    if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
    {
        jsoo = xmlHttp.responseText;
        var jsonobj = eval("("+jsoo+")");
        console.log(jsonobj);
        //console.log(jsonobj.data.pronunciations.uk);
        document.getElementById('wordcontent').innerText = jsonobj.data.content;
        document.getElementById('pronuciation_uk').innerText = jsonobj.data.pronunciations.uk;
        document.getElementById('pronuciation_us').innerText = jsonobj.data.pronunciations.us;
        document.getElementById('cn_definition').innerText = jsonobj.data.cn_definition.defn;
        document.getElementById('exm_sent1').innerText = jsonobj.data.object_id.data[0].annotation;
        document.getElementById('exm_sent2').innerText = jsonobj.data.object_id.data[1].annotation;
        document.getElementById('exm_sent3').innerText = jsonobj.data.object_id.data[2].annotation;
        document.getElementById('en_definition1').innerText = jsonobj.data.en_definitions.n[0];
        document.getElementById('en_definition2').innerText = jsonobj.data.en_definitions.n[1];
    }

}

