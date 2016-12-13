angular.module('UBCPIEN').
    directive('piAnswerResult', function(){
        return {
            restrict: 'E',
            scope: {
                legend: '@',
                options: '=',
                correct: '=',
                answer: '='
            },
            templateUrl: 'ubcpi-answer-result.html'
        }
    });
