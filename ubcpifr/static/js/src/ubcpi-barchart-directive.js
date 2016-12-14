angular.module('UBCPIFR').
    directive('piBarchart', function(){
        return {
            restrict: 'E',
            scope: {
                options: '=',
                stats: '=',
                correct: '=',
                answer: '=',
                role: '='
            },
            // no overwrite template
            replace: false,
            link: function(scope, element) {
                // watch the stats as it could be async populated
                scope.$watch('stats', function(stats) {
                    if(!stats) {
                        return;
                    }

                    var data = [];
                    for (var i = 0; i < scope.options.length; i++) {
                        data.push({
                            frequency: i in stats ? stats[i] : 0,
                            label: 'Choix ' + (i + 1) + (scope.correct == i ? ' (bonne réponse)' : ''),
                            class: 'ubcpibar' +  (scope.correct == i ? ' bonne réponse' : '')
                        });
                    }

                    // generate the chart
                    var chartLayout = d3.custom.barChart(scope);

                    d3.select(element[0])
                        .datum(data)
                        .call(chartLayout)
                }, true)
            }
        }
    });
