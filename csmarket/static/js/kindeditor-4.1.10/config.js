//news
KindEditor.ready(function(K) {
	K.create('textarea[name="new_content"]', {
		width : "800px",
        height : "500px",
		uploadJson: '/admin/uploads/kindeditor',
	});
});

//message
KindEditor.ready(function(K) {
	K.create('textarea[name="mess_content"]', {
		width : "800px",
        height : "500px",
		uploadJson: '/admin/uploads/kindeditor',
	});
});


// 技术文档
KindEditor.ready(function(K) {
	K.create('textarea[name="show"]', {
		width : "800px",
        height : "500px",
		uploadJson: '/admin/uploads/kindeditor',
	});
});

// 发布信息时
KindEditor.ready(function(K) {
	K.create('textarea[name="miaoshu"]', {
		width : "800px",
        height : "500px",
		uploadJson: '/admin/uploads/kindeditor',
	});
});