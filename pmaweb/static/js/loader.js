function cycleImages(){
      var $active = $('#cycler .active');
      var $next = ($active.next().length > 0) ? $active.next() : $('#cycler img:first');
      $next.css('z-index',2);//move the next image up the pile
      $active.fadeOut(1500,function(){//fade out the top image
	  $active.css('z-index',1).show().removeClass('active');//reset the z-index and unhide the image
          $next.css('z-index',3).addClass('active');//make the next image the top one
      });
    }

/**
 * Shows only subset of divs with class "theme" which have class passed
 * as a parameter.
 */
function showTheme(version) {
    $('.themelink').parent().removeClass('active');
    $('.themelink.' + version).parent().addClass('active');
    if (version === "all") {
        $(".themediv").show();
        return;
    }
    $(".themediv." + version).show();
    $(".themediv:not(." + version + ")").hide();
}

/* Auto load blocks */
$(function(){
    // run every 5s
    setInterval(cycleImages, 5000);

    // colorbox init
    $('.colorbox').colorbox({
        rel: 'gal',
        maxWidth: '100%',
        maxHeight: '100%',
        width: '100%',
        height: '100%',
        current: '{current}/{total}'
    });


    /* Theme loader */
    if ($(".themediv").length > 0) {

        var hash = null;

        /* Do we have some parameter? */
        if (self.document.location.hash.length > 1) {
            hash = self.document.location.hash.substring(1);
            /* Check validity */
            if (hash.match(/^(pma_[0-9]_[0-9]|all)$/) === null) {
                hash = null;
            }
        }
        if (hash === null) {
            hash = $('.themelink:last').data('theme');
        }

        /* Finally show chosen schema */
        showTheme(hash);

        $('.themelink').click(function () {
            showTheme($(this).data('theme'));
        });
    }

    $('.download_popup').click(function () {
        var $this = $(this);
        var pgp = $this.data('pgp');
        ga('send', 'event', 'Download', $this.attr('href').replace('https://files.phpmyadmin.net/', ''));
        $('#dl-link').attr('href', $this.attr('href'));
        $('#dl-sha256').text($this.data('sha256'));
        if (pgp !== '') {
            $('#dl-li-pgp').show();
            $('#dl-pgp').attr('href', pgp);
        } else {
            $('#dl-li-pgp').hide();
        }
        $('#downloadModal').modal('show');
    });

});
