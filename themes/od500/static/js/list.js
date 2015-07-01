(function(){
	var $container = $('.isotopes-container').isotope({
		layoutMode: 'fitRows',
		resizesContainer : false,
	});
    var filters = [];
    var filtr = '';


	// filter items on button click
	$('#filters-category').on( 'click', 'button', function( event ) {
        filtr = $(this).attr('data-filter');
        if ($(this).hasClass('s-active')) { //already active, deactivate
            $(this).removeClass('s-active');
            filters.splice(filters.indexOf($(this).attr('data-filter')), 1)
        } else { //not active, activate it
            $("#filters-category button").each(function() { //remove all previous filters of the kind
                var i = filters.indexOf($(this).attr('data-filter'));
                if( i > -1) {
                    filters.splice(i, 1)
                } 
            });
            filters.push(filtr);
            console.log(filters.join(''));
            //re-draw isotopes
            $("#filters-category button").removeClass('s-active');
            $(this).addClass('s-active');
        }
        $container.isotope({ filter: filters.join('') });
	});


    //filter by agency
    $('#filters-agency').on( 'click', 'button', function( event ) {
        filtr = $(this).attr('data-filter');
        if (filtr == "*") {
            $("#filters-agency button").each(function() { //remove all previous filters of the kind
                var i = filters.indexOf($(this).attr('data-filter'));
                if( i > -1) {
                    filters.splice(i, 1)
                }
                $(this).removeClass('s-active'); 
            });
        } else if ($(this).hasClass('s-active')) { //already active, deactivate
            $(this).removeClass('s-active');
            filters.splice(filters.indexOf($(this).attr('data-filter')), 1)
        } else { //not active, activate it
            filters.push(filtr);
            console.log(filters.join(''));
            //re-draw isotopes
            //$("#filters-category button").removeClass('s-active');
            $(this).addClass('s-active');
        }
        $container.isotope({ filter: filters.join('') });
    });

    // filter items by survey type
    $('.survey-filter').on( 'click', 'button', function( event ) {
        var filtr = $(this).attr('data-filter');
        if ($(this).hasClass('s-active')) {
            $(this).removeClass('s-active');
            filters.splice(filters.indexOf($(this).attr('data-filter')), 1)
        } else {
            $('.survey-filter button').each(function() {
                var i = filters.indexOf($(this).attr('data-filter'));
                if( i > -1) {
                    filters.splice(i, 1)
                }
            });
            $('.survey-filter button').removeClass('s-active');
            $(this).addClass('s-active');
            filters.push(filtr);
            console.log(filters.join(''))
        }
      $container.isotope({ filter: filters.join('') });
    });

    // filter items by company type
    $('.company-type-filter').on( 'click', 'button', function( event ) {
        var filtr = $(this).attr('data-filter');
        if ($(this).hasClass('s-active')) {
            $(this).removeClass('s-active');
            filters.splice(filters.indexOf($(this).attr('data-filter')), 1)
        } else {
            $('.company-type-filter button').each(function() {
                var i = filters.indexOf($(this).attr('data-filter'));
                if( i > -1) {
                    filters.splice(i, 1)
                }
            });
            $('.company-type-filter button').removeClass('s-active');
            $(this).addClass('s-active');
            filters.push(filtr);
            console.log(filters.join(''))
        }
      $container.isotope({ filter: filters.join('') });
    });

	// $container.delegate( '.m-candidates-item', 'click', function(){
	// 		//$('.m-candidates-item.large').removeClass('large');
	//         $(this).toggleClass('s-active');
	//         $container.isotope();
	// });
            
    // var userData = document.getElementById('hidden').textContent.replace('<','').replace('>','');
    // userData = JSON.parse(userData)
    // data = userData

    var data = statesForMap;

    createChart = function(){
        var hoverDisplay = "State &amp; Value".replace('&amp;', '&')
        
        //General chart
        this.Title = '500 Companies';
        this.Size = 600;
        this.MarginTop = 60;
        this.MarginRight = 0;
        this.MarginBottom = 40;
        this.MarginLeft = -61;
        this.Guide = false;
        this.DataType = 'Number';
        this.BackgroundColor = 'transparent';
        //States
        this.StateBaseColor = '#eeeeee';
        this.StateMaxColor = '#4a2f76';
        this.Range = 50;
        this.LineThickness = "1px";
        this.LineColor = '#888';
        //Labels
        this.ChartTitle = true;
        this.ChartTitleText = chartTitleText;
        this.ChartTitleXLocation = 'Center';
        this.ChartTitleYLocation = 0;
        this.ChartTitleFont = 'Arial';
        this.ChartTitleSize = 24;
        this.ChartTitleColor = '#472b74';
        this.PointLabel = true;
        this.PointLabelLocation = -10;
        this.PointLabelFont = 'Arial';
        this.PointLabelSize = 14;
        this.PointLabelColor = '#000000';
        //Hover State
        this.HoverStates = true;
        this.HoverDisplay = hoverDisplay;
        this.HoverLabelFont = 'Arial';
        this.HoverLabelSize = 10;
        this.HoverLabelColor = '#000000';
        this.HoverValueFont = 'Arial';
        this.HoverValueSize = 16;
        this.HoverValueColor = '#000000';
        
        this.mainChart = function() {
        
            var height = 550;
            var width = 950;
            
            var size = this.Size/width,
                marginTop = this.MarginTop,
                marginRight = this.MarginRight,
                marginBottom = this.MarginBottom,
                marginLeft = this.MarginLeft,
                guideOn = this.Guide,
                dataType = this.DataType,
                backgroundColor = this.BackgroundColor,
                stateBaseColor = this.StateBaseColor,
                stateMaxColor = this.StateMaxColor,
                range = this.Range,
                lineThickness = this.LineThickness,
                lineColor = this.LineColor,
                chartTitle = this.ChartTitle,
                chartTitleText = this.ChartTitleText,
                chartTitleXLoc = this.ChartTitleXLocation,
                chartTitleYLoc = this.ChartTitleYLocation,
                chartTitleFont = this.ChartTitleFont,
                chartTitleSize = this.ChartTitleSize,
                chartTitleColor = this.ChartTitleColor,
                pointLabelLoc = this.PointLabelLocation,
                pointLabelFont = this.PointLabelFont,
                pointLabelSize = this.PointLabelSize,
                pointLabelColor = this.PointLabelColor,
                hoverStates = this.HoverStates,
                hoverDisplay = this.HoverDisplay,
                hoverLabelFont = this.HoverLabelFont,
                hoverLabelSize = this.HoverLabelSize,
                hoverLabelColor = this.HoverLabelColor,
                hoverValueFont = this.HoverValueFont,
                hoverValueSize = this.HoverValueSize,
                hoverValueColor = this.HoverValueColor;
                
            var margin = {top: marginTop, right: marginRight, bottom: marginBottom, left: marginLeft},
                w = (width*size) + margin.left + margin.right,
                h = (height*size) + margin.top + margin.bottom;
                
            var bkgdColor = document.getElementsByTagName("body")[0];
            bkgdColor.setAttribute("style","background-color:" + backgroundColor + ";margin:0px;" + "font-size:12px;");

            var elem = document.getElementById("chart");
            elem.setAttribute("style","width:40% height:" + h + "px; margin: 0px;");
            
            var graph = d3.select('#chart').append('svg')
                .attr('width', w)
                .attr('height', h);
                
            //Background Color
            graph.append("svg:rect")
                .attr("class", "bkgd")
                .attr("width", w)
                .attr("height", h)
                .style("fill", "none");
                
            var group = graph.append('g');
            
            var hover = d3.select("#chart")
                .append("div")
                .attr("class", "tooltip")
                .style("position", "absolute")
                .style("z-index", "1000")
                .style("padding", "5px")
                .style("font-family", hoverLabelFont)
                .style("font-size", hoverLabelSize)
                .style("color", hoverLabelColor);
                
            queue()
                .defer(d3.json, "/data/" + country + "_states.json")
                .await(ready);
                
            var numberFormat = d3.format("0,000");
            var percentFormat = function(d) { return numberFormat(d) + "%"; };
            var dollarFormat = function(d) { return "$" + numberFormat(d); };
            
            var projection = d3.geo.albersUsa();
            var path = d3.geo.path()
                .projection(projection);
                
            group.attr('transform', 'translate(' + margin.left + ', ' + margin.top + '),scale(' + size + ', ' + size + ')');
            
            var colors = ['#fff', '#efedf5', '#dadaeb', '#bcbddc', 
                            '#9e9ac8', '#807dba', '#6a51a3', '#54278f',
                            '#3f007d']
            var maxVal = d3.max(data, function(d) { return d.VALUE; });
            var minVal = d3.min(data, function(d) { return d.VALUE; });
            var color = d3.scale.threshold()
                .domain([1, 2, maxVal/7, 2*maxVal/7, 3*maxVal/7, 4*maxVal/7, 5*maxVal/7, 6*maxVal/7, maxVal+1 ])
                .range(colors);
            
            var number = d3.format("0,000");
            
            function ready(error, us, _data) {
            
                group.selectAll('path')
                    .data(us.features)
                    .enter().append('path')
                    .attr('class', 'states')
                    .attr('d', d3.geo.path().projection(projection))
                    .attr('name', function(d){ return d.properties.NAME})
                    .style('stroke', lineColor)
                    .style('stroke-width', lineThickness);
                    
                var states = group.selectAll('.states')
                    .data(data, function(d) { return (d && d.STATE) || d3.select(this).attr("name"); })
                    .style("fill", function(d) { return color(d.VALUE); })
                    .attr('abbrev', function(d) { return d.abbrev; })
                    .on("mouseover", function(d, i) {   
                        hover.transition().duration(100).style("opacity", 1)
                            .style("background-color", "#aaaaaa")
                            .style("left", (d3.event.pageX) + 20 + "px")
                            .style("top", (d3.event.pageY) + "px");
                        hover.html(d.STATE + "<br><span style='font-size:" + hoverValueSize + "; font-family:" + hoverValueFont + ";color:" + hoverValueColor + ";'>" + numberFormat(d.VALUE) + "</span>");
                    })
                    .on("mouseout", function(d) { if (hoverStates == true) hover.style("left", -100).style("top", -100).transition().duration(100).style("opacity", 0); })
                    .on("mousemove", function(d, i) { if (hoverStates == true)hover.style("left", (d3.event.pageX) + 20 + "px").style("top", (d3.event.pageY) + "px"); });
                
                states.on('click', function(s) {
                    var filtr = '.' + this.getAttribute('abbrev');
                    if(this.attributes.class.value == "states s-active") { //if clicking on the same state, remove active class and remove filter from filters
                        filters.splice(filters.indexOf('.'+s.abbrev), 1);
                        d3.select(this)
                            .attr("class", "states")
                            .style("stroke", lineColor)
                            .style("stroke-width", lineThickness)
                    } else { //state previously inactive, activate, and remove from filter list
                        d3.select(this).attr("class", "states s-active")
                        d3.selectAll('.states')
                            .each(function(d) { 
                                var i = filters.indexOf('.'+d.abbrev)
                                if (i > -1) { //remove all states in filter array
                                    filters.splice(i, 1);
                                }
                            })
                            .filter(function(d, i) { return  d != s }) //remove active class from other states
                            .attr("class", "states")
                            .style("stroke", lineColor)
                            .style("stroke-width", lineThickness);
                        filters.push(filtr);
                    }
                    d3.select(".states.s-active").style("stroke", "black").style("stroke-width", 4)
                    $container.isotope({ filter: filters.join('') });
                });

                //clear filters
                $('#legend').on("click", ".clear-all-filters", function(event) {
                    filters = [];
                    d3.select(".states.s-active")
                    .style("stroke", '#888')
                    .style("stroke-width", lineThickness);
                    $('.s-active').removeClass('s-active');
                    $container.isotope({ filter: '' });
                });

                if (chartTitleXLoc == "Left") { var cxpos = margin.left; var ctextanchor = "start"; };
                if (chartTitleXLoc == "Center") { var cxpos = (w - margin.right - margin.left)/2 + margin.left; var ctextanchor = "middle"; };
                if (chartTitleXLoc == "Right") { var cxpos = (w - margin.right - margin.left) + margin.left; var ctextanchor = "end"; };
                
                if (chartTitle == true) {
                graph.append("text")
                    .attr("transform", "translate(" + cxpos + "," + (margin.top + chartTitleYLoc) + ")")
                    .style({ 'text-anchor': ctextanchor, 'font-family': chartTitleFont, 'font-size': chartTitleSize, 'fill': chartTitleColor})
                    .text(chartTitleText);
                }
                
            }
            
        };
        
            this.updateChart = function(){
                d3.select("svg").remove()
                this.mainChart()
            };  
        };
        
    var chart = new createChart()         
    chart.mainChart()
})()
