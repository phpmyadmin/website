// ------------------------------------------------------------------
// AUTHOR: Ryan J. Salva
// MODIFIED: December 22, 2007
//
// DESCRIPTION:
// creates a single, rotating image on a page
//
// IMPLEMENTATION:
// <div id="Container">
// <img src="1.jpg" /><img src="2.jpg" /><img src="3.gif" />
// </div>
// <script type="text/javascript">
// window.addEvent('domready',function() {
// var f = new Fader('Container');
// f.start();
// });
// </script>


var Fader = new Class({
        Implements: Options,
        options: {
                pause: 5000,
                duration: 1000,
                loop: true,
                onComplete: Class.empty,
                onStart: Class.empty
        },
        initialize: function(container,options) {
                this.setOptions(options);
                this.container = $(container);
                this.imgs = this.container.getElements('img');
                this.imgs.setStyles({
                        'position':'absolute',
                        'top':0,
                        'left':0,
                        'opacity':0
                });
                this.imgs[0].setStyle('opacity',1);
                this.el = new Element('div',{'styles': {
                        'position':'relative'
            }});
            this.el.injectInside(this.container);
            this.el.adopt(this.imgs);
                this.next = 0;
                this.start();
        },
        start: function() {
                this.periodical = this.show.bind(this).periodical(this.options.pause);
        },
        stop: function() {
                $clear(this.periodical);
        },
        show: function() {
                if (!this.options.loop && this.next==this.imgs.length-1) this.stop();
                this.next = (this.next==this.imgs.length-1)?0:this.next+1;
                var prev = (this.next==0)?this.imgs.length-1:this.next-1;

                this.imgs[this.next].fade('in');
                this.imgs[prev].fade('out');
        }
}); 
