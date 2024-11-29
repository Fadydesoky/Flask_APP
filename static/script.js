// حدث يتم تشغيله عندما يتم تحميل الصفحة بالكامل
document.addEventListener("DOMContentLoaded", function() {
    console.log("Page has loaded!");
});

// بعد تحميل الصفحة
document.addEventListener("DOMContentLoaded", function() {
    // تحديد جميع العناصر من نوع li في الصفحة
    const dataItems = document.querySelectorAll("li");
    
    // إضافة حدث عند النقر على أي عنصر li
    dataItems.forEach(item => {
        item.addEventListener("click", function() {
            alert("You clicked on a data item!");
        });
    });
});


// بعد تحميل الصفحة
document.addEventListener("DOMContentLoaded", function() {
    // تحديد العنصر الذي يحتوي على النص
    const title = document.querySelector("h1");

    // إضافة حدث عند النقر على العنصر
    title.addEventListener("click", function() {
        title.textContent = "You clicked the title!";
    });
});
