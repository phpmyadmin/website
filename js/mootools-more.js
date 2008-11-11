//MooTools More, <http://mootools.net/more>. Copyright (c) 2006-2008 Valerio Proietti, <http://mad4milk.net>, MIT Style License.

var Tips=new Class({Implements:[Events,Options],options:{onShow:function(A){A.setStyle("visibility","visible");},onHide:function(A){A.setStyle("visibility","hidden");
},showDelay:100,hideDelay:100,className:null,offsets:{x:16,y:16},fixed:false},initialize:function(){var C=Array.link(arguments,{options:Object.type,elements:$defined});
this.setOptions(C.options||null);this.tip=new Element("div").inject(document.body);if(this.options.className){this.tip.addClass(this.options.className);
}var B=new Element("div",{"class":"tip-top"}).inject(this.tip);this.container=new Element("div",{"class":"tip"}).inject(this.tip);var A=new Element("div",{"class":"tip-bottom"}).inject(this.tip);
this.tip.setStyles({position:"absolute",top:0,left:0,visibility:"hidden"});if(C.elements){this.attach(C.elements);}},attach:function(A){$$(A).each(function(D){var G=D.retrieve("tip:title",D.get("title"));
var F=D.retrieve("tip:text",D.get("rel")||D.get("href"));var E=D.retrieve("tip:enter",this.elementEnter.bindWithEvent(this,D));var C=D.retrieve("tip:leave",this.elementLeave.bindWithEvent(this,D));
D.addEvents({mouseenter:E,mouseleave:C});if(!this.options.fixed){var B=D.retrieve("tip:move",this.elementMove.bindWithEvent(this,D));D.addEvent("mousemove",B);
}D.store("tip:native",D.get("title"));D.erase("title");},this);return this;},detach:function(A){$$(A).each(function(C){C.removeEvent("mouseenter",C.retrieve("tip:enter")||$empty);
C.removeEvent("mouseleave",C.retrieve("tip:leave")||$empty);C.removeEvent("mousemove",C.retrieve("tip:move")||$empty);C.eliminate("tip:enter").eliminate("tip:leave").eliminate("tip:move");
var B=C.retrieve("tip:native");if(B){C.set("title",B);}});return this;},elementEnter:function(B,A){$A(this.container.childNodes).each(Element.dispose);
var D=A.retrieve("tip:title");if(D){this.titleElement=new Element("div",{"class":"tip-title"}).inject(this.container);this.fill(this.titleElement,D);}var C=A.retrieve("tip:text");
if(C){this.textElement=new Element("div",{"class":"tip-text"}).inject(this.container);this.fill(this.textElement,C);}this.timer=$clear(this.timer);this.timer=this.show.delay(this.options.showDelay,this);
this.position((!this.options.fixed)?B:{page:A.getPosition()});},elementLeave:function(A){$clear(this.timer);this.timer=this.hide.delay(this.options.hideDelay,this);
},elementMove:function(A){this.position(A);},position:function(D){var B=window.getSize(),A=window.getScroll();var E={x:this.tip.offsetWidth,y:this.tip.offsetHeight};
var C={x:"left",y:"top"};for(var F in C){var G=D.page[F]+this.options.offsets[F];if((G+E[F]-A[F])>B[F]){G=D.page[F]-this.options.offsets[F]-E[F];}this.tip.setStyle(C[F],G);
}},fill:function(A,B){(typeof B=="string")?A.set("html",B):A.adopt(B);},show:function(){this.fireEvent("show",this.tip);},hide:function(){this.fireEvent("hide",this.tip);
}});