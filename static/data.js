// document.getElementById("form11").addEventListener("click",make);
// document.getElementById("data2").addEventListener("click",make);
// let td=document.getElementById("id1")
// let r=document.getElementById("id2")

// function make(){
//  console.log("i am kenil"); 
//  const kenil=new XMLHttpRequest();
//  kenil.open("POST","",true)
//  kenil.onreadystatechange=function(){
//      if(kenil.readyState === XMLHttpRequest.DONE){
//          if(kenil.status === 200){
//              console.log(kenil);
//              console.log(kenil.responseText);
//              td.innerText=kenil.response;
//              r.innerText=kenil.response;
//          }
//          else{
//              console.log("problem with response");
//          }
//      }
//  };
//  kenil.send();
// }

// <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
// $("#data1").on('click',function(e){
//     e.preventDefault();
//     $( "#main1" ).load( "facultyDashbord.html" );
//     alert("Page loading completed");  
// });


// function updateDB() {
//     const xhr = new XMLHttpRequest();
//     xhr.open("POST","facultyDashbord.html", true);
//     xhr.send();
//     /* ignore result */
// }

// $(document).ready(function(){
//     $.ajax({ url: "facultyDashbord.html",
//         context: document.body,
//         success: function(){
//            alert("done");
//         }
//     }); 
// });

// window.onload=function(){
//     $("#data1").click();
//     }   

// $(document).ready(function(){
//     $("button").click(function(){
//         $("#student.application_id").load("facultyDashbord.html");
//     });
// }); 


    // $('#{{ student.application_id }}').click(function () {
    //   console.log("save button clickd");
    // });

    // $('#form_post').on('submit', function(event){
    //     event.preventDefault();
    //     console.log("form submitted!")  // sanity check
    //     create_post();
    // });

  
