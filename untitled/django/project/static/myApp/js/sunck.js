console.log("Linuxcao is a good man")
console.log("Linuxcao is a nice man")
$(document).ready(function () {
    document.getElementById("btn").onclick =
        function () {
                $.ajax({
                    type: "get",
                    url:"/studentsinfo/",
                    dataType:"json",
                    success:function (data,status) {
                            console.log(data)
                            var d = data["data"]
                            for(var i=0;i<d.length;i++)
                            {
                                document.write('<p>'+d[i][0]+'</p>')
                            }
                        }
                       })
                    }
})