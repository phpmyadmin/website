{% for release in releases_featured %}
var PMA_latest_version = '${release.version}';
var PMA_latest_date = '${release.date.datestring()}';
{% end %}
