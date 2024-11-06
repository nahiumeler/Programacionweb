//Este tiene todo el código de Javascript
//console.log('Hello world!');
/*Con Esto puedo ver si está andando jquery
$(function(){
	console.log('JQuery esta funcionando')
});*/

$(document).ready(function(){
	var TotalVenta=0;//Variable global para mantener un contador de productos que el cliente fué agregando 
	let edit = false;
	var listaProductos = [];
	 
	console.log('JQuery esta funcionando');
	$('#task-result').hide();//Ocultamos el elemento card

	fetchArticulos(); //Llamamos a la función definida aquí mismo para que se ejecute apenas entra

	//$('#search').keyup(function(e){
	//$(document).on('keyup', '.idCantidad', function(){
	$("#productos").on("keyup", ".idCantidad", function(e){
		
		if(e.keyCode==13){
			let idProducto = $(this)[0].parentElement.parentElement.cells[0].innerHTML;
			let descripcion = $(this)[0].parentElement.parentElement.cells[2].innerHTML;
			let txtCantidad = $(this);
			let cantidad = txtCantidad.val();
			let precioMayorista = $(this)[0].parentElement.parentElement.cells[3].innerHTML;
			let subtotal = precioMayorista * cantidad;
			//redondeo a 2 decimales
			subtotal = subtotal.toFixed(2);

			$(this)[0].parentElement.parentElement.cells[5].innerHTML = subtotal;
			
			txtCantidad.blur();
			agregarAlCarrito(idProducto, descripcion, precioMayorista, cantidad, subtotal);
		}

	});

	function agregarAlCarrito(idProducto, descripcion, precio, cantidad, subtotal){
		let cantProductos = 0;//Contador de productos

		cantProductos = $('#bdgCantProductos').html();
		cantProductos++;
		$('#bdgCantProductos').html(cantProductos);
		//Utilizo un id único de fila, que lo hago con el contador de productos, para luego poder eliminar
		let fila = `<tr idProdModal=${cantProductos}>
						<td>${idProducto}</td>
						<td>${descripcion}</td>
						<td>${precio}</td>
						<td>${cantidad}</td>
						<td>${subtotal}</td>
						<td>
							<button class = "producto-quitar btn btn-danger btn-sm">
								Quitar
							</button>
						</td>
					</tr>`;
		$('#tbPedidosEnCurso').append(fila);

		TotalVenta = parseFloat(TotalVenta) + parseFloat(subtotal);

		var strTotal = "Total: $" + TotalVenta; 
		$('#total').html(strTotal);
		$('#totalModal').html(strTotal);

		let producto = {
			"idProducto": idProducto,
			"descripcion": descripcion,
			"precio": precio,
			"cantidad": cantidad,
			"subtotal": subtotal
		   }

		   listaProductos.push(productos);
		   
	}

	//Este evento es para quitar un producto cargado
	$(document).on('click', '.producto-quitar', function(){
		let idProducto = $(this)[0].parentElement.parentElement.cells[0].innerHTML;;
		let cantProductos = 0;//Contador de productos
		let subtotalProducto = $(this)[0].parentElement.parentElement.cells[4].innerHTML;
		let element = $(this)[0].parentElement.parentElement;//Referencia a la fila contenedora del botón para eliminar
		var strTotal;

		cantProductos = $('#bdgCantProductos').html();
		cantProductos--;
		$('#bdgCantProductos').html(cantProductos);
		
		TotalVenta = (parseFloat(TotalVenta) - parseFloat(subtotalProducto)).toFixed(2);
		var strTotal = "Total: $" + TotalVenta;
		$('#total').html(strTotal);
		$('#totalModal').html(strTotal);

		element.remove();

		//Restablecemos la cantidad y precio total de la lista principal
		let elemento = '#producto_'+idProducto;
		$(elemento)[0].cells[4].children[0].value="";
		$(elemento)[0].cells[5].innerHTML = "";
	}); 

	$('#carrito').click(function(e){
	//$("#carrito").on("click", ".btn btn-success", function () {
		console.log("Llamo al evento click del boton de carrito");
		//$('[data-toggle="popover"]').popover();
	  });
	
	//Para levantar los artículos
	function fetchArticulos(){
		$.ajax({ 
			//url: 'php/listar-productos.php',
			url: '/listar',
			type: 'GET',
			success: function (response){
				console.log(response);
				//let productos = JSON.parse(response);
				let productos = response;
				console.log(productos);
				
				let template = '';
				productos.forEach(producto => {
					template += `
						<tr id=producto_${producto.idProducto}>
							<td>${producto.idProducto}</td>
							<td class="thumbnail"><img src="${producto.foto}" alt=""></td>
							<td>
								<a href="#" class="producto-item">${producto.descripcion}</a>
							</td>
							<td>${producto.precioMayorista}</td>
							<td><input type="text" class="idCantidad form-control mr-xs-2" placeholder="Cantidad"></td>
							<td></td>
							<td>${producto.categorias}</td>
						</tr>
					`
				})
				$('#productos').html(template); //Utilizamos el elemento del id del tbody y modificamos en el dom
	
			}
		});
	}

	function registarPedido() {
		
		$.ajax({
			type: "POST",
			url: "/registrar_pedido",
			dataType: "json",
			success: function (msg) {
				if (msg) {
					alert("Se agregó el pedido");
					location.reload(true);
				} else {
					alert("No se pudo agregar");
				}
			},
			data: listaProductos
		});
	}
	
});