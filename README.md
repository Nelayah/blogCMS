# 博客 - API服务端
The api server is built with django, django-restframework and postgresql.

## 后端
1. postgresql，建立文章，日记和杂事的表。字段记录标题，标签，slug，摘要，文本内容和创建的时间。
2. 建立图床Gallery的表，存放自己图片静态资源。
3. HTTP SAFE METHON只开放get请求。
4. 使用django自带的admin界面作CMS，对网站CMS做管理。

## 前端
[BLOG FRONTEND](https://github.com/Nelayah/blog)

## License

Copyright © 2017, 彭加生 (hayalen < hayaleNelayah@outlook.com >). All Rights Reserved.
This project is free software and released under the **[GNU General Public License (GPL V3)](http://www.gnu.org/licenses/gpl.html)**.
