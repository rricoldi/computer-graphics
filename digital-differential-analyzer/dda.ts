interface IPoint {
  x: number;
  y: number;
}

const getRoundedPoint = (point: IPoint): IPoint => ({
  x: Math.round(point.x),
  y: Math.round(point.y)
});

function dda(start: IPoint, end: IPoint): IPoint[] {
  const linePoints = [ start ];

  const currentPoint: IPoint = { ...start };

  const deltaX = Math.abs(end.x - start.x);
  const deltaY = Math.abs(end.y - start.y);
  
  const step = deltaY > deltaX ? deltaY : deltaX;

  const xIncrement = (end.x - start.x)/step;
  const yIncrement = (end.y - start.y)/step;

  while(currentPoint.x < end.x) {
    currentPoint.x = currentPoint.x + xIncrement;
    currentPoint.y = currentPoint.y + yIncrement;

    linePoints.push(
      getRoundedPoint(currentPoint)
    );
  }

  return linePoints;
}

if(Deno.args.length < 4) {
  console.log('Por favor insira os pontos de início e fim da reta a ser calculada');
} else {
  const startPoint = {
    x: Number(Deno.args[0]),
    y: Number(Deno.args[1]),
  };
  
  const endPoint = {
    x: Number(Deno.args[2]),
    y: Number(Deno.args[3]),
  };
  
  
  const linePoints = dda(startPoint, endPoint);
  
  linePoints.forEach(point => {
    console.log(`(${point.x}, ${point.y})`)
  });
}