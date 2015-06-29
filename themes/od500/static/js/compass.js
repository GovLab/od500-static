/*globals $, d3, console*/
/*jshint camelcase:false, browser: true, curly: false, maxlen: 1000,
maxstatements: 1000, eqeqeq: false */

$('.m-homepage').css('text-align', 'left' );

function draw_diagram(data) {

    function groupTicks(d) {
      var k = (d.endAngle - d.startAngle) / d.value;
      return d3.range(0, d.value, 1000).map(function(v) {
        return {
          angle: v * k + d.startAngle + (d.endAngle - d.startAngle)/2,
          label: data.names[d.index],
          angleDiff: d.endAngle - d.startAngle
        };
      });
    }

    function mouseover(d, i) {
      chord.classed("fade", function(p) {
        return p.source.index != i && p.target.index != i;
      });
    }

    var chord = d3.layout.chord()
        .padding(0.01)
        .sortSubgroups(d3.descending)
        .matrix(data.matrix);

    var width = 730,
        height = 750,
        innerRadius = Math.min(width, height) * 0.25,
        outerRadius = innerRadius * 1.14;

    var maxColor = '#4a2f76';
    var baseColor = '#eeeeee';
    var baseColor2 = '#a9db6c';
    var range = 50;
    //var maxVal = d3.max(chord.groups, function(d) { return d.value; });
    //var minVal = d3.min(chord.groups, function(d) { return d.value; });
    var fill_agencies = d3.scale.linear().domain([0,range]).range([maxColor, baseColor]);
    var fill_categories = d3.scale.linear().domain([0,range]).range([maxColor, baseColor2]);

    var svg = d3.select("#chord-chart").append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("id", "circle")
      .append("g")
        .attr("transform", "translate(335, 375)");
        // .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    svg.append("circle")
        .attr("r", outerRadius);

    svg.append("g").selectAll("path")
        .data(chord.groups)
        .enter().append("path")
        .style("fill", function(d) {
            if (data.num_agencies > d.index) {
                return fill_agencies(d.index);
            } else {
                return fill_categories(d.index);
            }
        })
        .attr("d", d3.svg.arc().innerRadius(innerRadius).outerRadius(outerRadius))
        .on("mouseover", mouseover);

    var ticks = svg.append("g").selectAll("g")
        .data(chord.groups)
        .enter().append("g").selectAll("g")
        .data(groupTicks)
        .enter().append("g")
        .attr("transform", function(d) {
          return "rotate(" + (d.angle * 180 / Math.PI - 90) + ")" +
              "translate(" + outerRadius + ",0)"; });

    ticks.append("text")
        .attr("x", 8)
        .attr("dy", ".35em")
        .attr("transform", function(d) { return d.angle > Math.PI ? "rotate(180)translate(-16)" : null; })
        .style("text-anchor", function(d) { return d.angle > Math.PI ? "end" : null; })
        .text(function(d) { return d.label; })
        .filter(function(d) { return d.angleDiff < 0.017; })
        .remove();

    //var chord = svg.append("g")
    chord = svg.selectAll(".chord")
      //.selectAll("path")
        .data(chord.chords)
      .enter().append("path")
        .attr("class", "chord")
        .attr("d", d3.svg.chord().radius(innerRadius))
        .style("fill", "rgba(0,0,0,0.2)");
        // .style("fill", function(d) {
        //     return fill_agencies(d.target.index);
        // });

    chord.on("mouseover", function() {
        d3.select(this).style("fill", "rgba(0,0,0,0.4)");
    }).on("mouseout", function() {
        d3.select(this).style("fill", "rgba(0,0,0,0.1)");
        // d3.select(this).style("fill", function(d) {
        //     return fill_agencies(d.target.index);
        // });
    });

    chord.append("title")
        .text(function(d) {
            return data.names[d.source.index] + "->" + data.names[d.target.index] + "\n" + d.target.value + " companies";
        });

    // nodes.append("title")
    //     .text(function(d) { return data.names[d.index] + "\n" + d.value + " companies"});

}

d3.json($('#chord-chart').data('matrix-json'), function(error, json) {
    if (error) return console.warn(error);
    draw_diagram(json);
});
